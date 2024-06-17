
from typing import Optional, Union, overload

import torch


_Size = torch.Size
_device = torch.device
Tensor = torch.Tensor


class COOTensor():
    def __init__(self, indices: Tensor, values: Optional[Tensor],
                 spshape: Optional[_Size]=None, *,
                 is_coalesced: Optional[bool]=None):
        """
        Initialize COO format sparse tensor

        Parameters:
            indices (Tensor): indices of non-zero elements, shaped (D, N).
                Where D is the number of sparse dimension, and N is the number
                of non-zeros (nnz).
            values (Tensor | None): non-zero elements, shaped (..., N).
            spshape (Size | None): shape in the sparse dimensions.
        """
        self.indices = indices
        self.values = values
        self.is_coalesced = is_coalesced

        if spshape is None:
            self._spshape = torch.Size(torch.max(indices, dim=1)[0] + 1)
        else:
            self._spshape = torch.Size(spshape)

        self._check(indices, values, spshape)

    def _check(self, indices: Tensor, values: Optional[Tensor], spshape: _Size):
        if not isinstance(indices, Tensor):
            raise TypeError(f"indices must be a Tensor, but got {type(indices)}")
        if indices.ndim != 2:
            raise ValueError(f"indices must be a 2D tensor, but got {indices.ndim}D")

        # total ndim should be equal to sparse_ndim + dense_dim
        if len(spshape) != indices.shape[0]:
            raise ValueError(f"size must have length {indices.shape[0]}, "
                             f"but got {len(spshape)}")

        if isinstance(values, Tensor):
            if values.ndim < 1:
                raise ValueError(f"values must be at least 1D, but got {values.ndim}D")

            # The last dim of values must match the last dim of indices.
            if values.shape[-1] != indices.shape[1]:
                raise ValueError(f"values must have the same length as indices ({indices.shape[1]}) "
                                 "in the last dimension (number of non-zero elements), "
                                 f"but got {values.shape[-1]}")
        elif values is None:
            pass
        else:
            raise TypeError(f"values must be a Tensor or None, but got {type(values)}")

    def __repr__(self) -> str:
        return f"COOTensor(indices={self.indices}, values={self.values}, shape={self.shape})"

    @overload
    def size(self) -> _Size: ...
    @overload
    def size(self, dim: int) -> int: ...
    def size(self, dim: Optional[int]=None):
        if dim is None:
            return self.shape
        else:
            return self.shape[dim]

    @property
    def device(self): return self.indices.device
    @property
    def dtype(self):
        if self.values is None:
            return self.indices.dtype
        else:
            return self.values.dtype

    @property
    def shape(self):
        if self.values is None:
            return self._spshape
        else:
            return torch.Size(self.values.shape[:-1] + self._spshape)

    @property
    def dense_shape(self): return self.values.shape[:-1]
    @property
    def sparse_shape(self): return self._spshape

    @property
    def ndim(self):
        if self.values is None:
            return self.sparse_ndim
        else:
            return self.dense_ndim + self.sparse_ndim

    @property
    def dense_ndim(self): return self.values.ndim - 1
    @property
    def sparse_ndim(self): return self.indices.shape[0]
    @property
    def nnz(self): return self.indices.shape[1]

    def clone_indices(self):
        """Return the indices of the non-zero elements."""
        return self.indices.clone()

    def clone_values(self):
        """Return the non-zero elements."""
        if self.values is None:
            return None
        else:
            return self.values.clone()

    def to_dense(self):
        """Convert the COO tensor to a dense tensor and return as a new object."""
        kwargs = {'dtype': self.dtype, 'device': self.device}
        dense_tensor = torch.zeros(self.shape, **kwargs)
        slicing = [self.indices[i] for i in range(self.sparse_ndim)]

        if self.values is None:
            dense_tensor[slicing] = 1
        else:
            slicing = [slice(None),] * self.dense_ndim + slicing
            dense_tensor[slicing] = self.values

        return dense_tensor

    def to(self, device: Union[_device, str, None]=None, non_blocking: bool=False):
        """Return a new COOTensor object with the same indices and values on the
        specified device."""
        pass

    def coalesce(self, accumulate: bool=True):
        """Merge duplicate indices and return as a new COOTensor object.

        Parameters:
            accumulate (bool, optional): Whether to count the occurrences of indices\
            as new values when `self.values` is None. Defaults to True.

        Returns:
            COOTensor: coalesced COO tensor.
        """
        kwargs = {'dtype': self.dtype, 'device': self.device}

        unique_indices, inverse_indices = torch.unique(
            self.indices, return_inverse=True, dim=1
        )

        if self.values is not None:
            dense_ndim = self.dense_ndim
            value_shape = self.dense_shape + (unique_indices.size(0), )
            new_values = torch.zeros(value_shape, **kwargs)
            inverse_indices = inverse_indices[(None,) * dense_ndim + (slice(None),)]
            inverse_indices = inverse_indices.broadcast_to(self.values.shape)
            new_values.scatter_add_(-1, inverse_indices, self.values)

            return COOTensor(
                unique_indices, new_values, self.sparse_shape, is_coalesced=True
            )

        else:
            if accumulate:
                ones = torch.ones((self.nnz, ), **kwargs)
                new_values = torch.zeros((unique_indices.size(0), ), **kwargs)
                new_values.scatter_add_(-1, inverse_indices, ones)
            else:
                new_values = None

            return COOTensor(
                unique_indices, new_values, self.sparse_shape, is_coalesced=True
            )