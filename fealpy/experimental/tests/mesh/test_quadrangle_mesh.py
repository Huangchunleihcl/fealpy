import numpy as np
import matplotlib.pyplot as plt
import pytest
from fealpy.experimental.backend import backend_manager as bm
from fealpy.experimental.mesh.quadrangle_mesh import QuadrangleMesh
from fealpy.experimental.tests.mesh.quadrangle_mesh_data import *


class TestQuadrangleMeshInterfaces:
    @pytest.mark.parametrize("backend", ['numpy', 'pytorch', 'jax'])
    @pytest.mark.parametrize("meshdata", init_mesh_data)
    def test_init(self, meshdata, backend):
        node = bm.from_numpy(meshdata['node'])
        cell = bm.from_numpy(meshdata['cell'])

        mesh = QuadrangleMesh(node, cell)

        assert mesh.number_of_nodes() == meshdata["NN"]
        assert mesh.number_of_edges() == meshdata["NE"]
        assert mesh.number_of_faces() == meshdata["NF"]
        assert mesh.number_of_cells() == meshdata["NC"]
        face2cell = mesh.face2cell
        np.testing.assert_array_equal(bm.to_numpy(face2cell), meshdata["face2cell"])

    @pytest.mark.parametrize("backend", ['numpy', 'pytorch', 'jax'])
    @pytest.mark.parametrize("meshdata", box_data)
    def test_from_box(self, meshdata, backend):
        box = bm.from_numpy(meshdata['box'])
        nx = bm.from_numpy(meshdata['nx'])
        ny = bm.from_numpy(meshdata['ny'])
        mesh = QuadrangleMesh.from_box(box, nx, ny)

        assert mesh.number_of_nodes() == meshdata["NN"]
        assert mesh.number_of_edges() == meshdata["NE"]
        assert mesh.number_of_faces() == meshdata["NF"]
        assert mesh.number_of_cells() == meshdata["NC"]

        node = mesh.node
        np.testing.assert_array_equal(bm.to_numpy(node), meshdata["node"])
        cell = mesh.cell
        np.testing.assert_array_equal(bm.to_numpy(cell), meshdata["cell"])
        face2cell = mesh.face2cell
        np.testing.assert_array_equal(bm.to_numpy(face2cell), meshdata["face2cell"])

    @pytest.mark.parametrize("backend", ['numpy', 'pytorch', 'jax'])
    @pytest.mark.parametrize("meshdata", entity_data)
    def test_entity(self, meshdata, backend):
        node = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=np.float64)
        cell = np.array([[0, 1, 2, 3]], dtype=np.int32)
        mesh = QuadrangleMesh(node, cell)
        q = 2

        assert mesh.entity_measure(0) == meshdata["entity_measure"][0]
        assert all(mesh.entity_measure(1) == meshdata["entity_measure"][1])
        assert all(mesh.entity_measure('cell') == meshdata["entity_measure"][2])

        integrator = mesh.quadrature_formula(q)
        bcs, ws = integrator.get_quadrature_points_and_weights()

        np.testing.assert_allclose(bm.to_numpy(bcs), meshdata["bcs"], atol=1e-7)
        np.testing.assert_allclose(bm.to_numpy(ws), meshdata["ws"], atol=1e-7)

        point = mesh.bc_to_point(bcs)
        np.testing.assert_allclose(bm.to_numpy(point), meshdata["point"], atol=1e-7)

    @pytest.mark.parametrize("backend", ['numpy', 'pytorch', 'jax'])
    @pytest.mark.parametrize("meshdata", geo_data)
    def test_geo(self, meshdata, backend):
        node = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=np.float64)
        cell = np.array([[0, 1, 2, 3]], dtype=np.int32)
        mesh = QuadrangleMesh(node, cell)

        edge_frame = mesh.edge_frame()
        edge_unit_normal = mesh.edge_unit_normal()

        np.testing.assert_allclose(bm.to_numpy(edge_frame), meshdata["edge_frame"], atol=1e-7)
        np.testing.assert_allclose(bm.to_numpy(edge_unit_normal), meshdata["edge_unit_normal"], atol=1e-7)

    @pytest.mark.parametrize("backend", ['numpy', 'pytorch', 'jax'])
    @pytest.mark.parametrize("meshdata", cal_data)
    def test_cal_data(self, meshdata, backend):
        node = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=np.float64)
        cell = np.array([[0, 1, 2, 3]], dtype=np.int32)
        bcs = (bm.tensor([[0.78867513, 0.21132487], [0.21132487, 0.78867513]], dtype=bm.float64),
               bm.tensor([[0.78867513, 0.21132487], [0.21132487, 0.78867513]], dtype=bm.float64))
        mesh = QuadrangleMesh(node, cell)

        shape_function = mesh.shape_function(bcs)
        np.testing.assert_allclose(bm.to_numpy(shape_function), meshdata["shape_function"], atol=1e-7)
        grad_shape_function = mesh.grad_shape_function(bcs)
        np.testing.assert_allclose(bm.to_numpy(grad_shape_function), meshdata["grad_shape_function"], atol=1e-7)
        grad_shape_function_x = mesh.grad_shape_function(bcs, variables='x')
        np.testing.assert_allclose(bm.to_numpy(grad_shape_function_x), meshdata["grad_shape_function_x"], atol=1e-7)

        jacobi_matrix = mesh.jacobi_matrix(bcs)
        np.testing.assert_allclose(bm.to_numpy(jacobi_matrix), meshdata["jacobi_matrix"], atol=1e-7)
        first_fundamental_form = mesh.first_fundamental_form(jacobi_matrix)
        np.testing.assert_allclose(bm.to_numpy(first_fundamental_form), meshdata["first_fundamental_form"], atol=1e-7)

    @pytest.mark.parametrize("backend", ['numpy', 'pytorch', 'jax'])
    @pytest.mark.parametrize("meshdata", extend_data)
    def test_extend_data(self, meshdata, backend):
        node = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=np.float64)
        cell = np.array([[0, 1, 2, 3]], dtype=np.int32)
        mesh = QuadrangleMesh(node, cell)
        p = meshdata["p"]

        assert mesh.number_of_global_ipoints(p) == meshdata["number_of_global_ipoints"]
        assert mesh.number_of_local_ipoints(p) == meshdata["number_of_local_ipoints"]
        assert mesh.number_of_corner_nodes() == meshdata["number_of_corner_nodes"]

        # 不兼容 jax
        # cell_to_ipoint = mesh.cell_to_ipoint(p)
        # np.testing.assert_allclose(bm.to_numpy(cell_to_ipoint), meshdata["cell_to_ipoint"], atol=1e-7)

        interpolation_points = mesh.interpolation_points(p)
        np.testing.assert_allclose(bm.to_numpy(interpolation_points), meshdata["interpolation_points"], atol=1e-7)

        jacobi_at_corner = mesh.jacobi_at_corner()
        np.testing.assert_allclose(bm.to_numpy(jacobi_at_corner), meshdata["jacobi_at_corner"], atol=1e-7)

        angle = mesh.angle()
        np.testing.assert_allclose(bm.to_numpy(angle), meshdata["angle"], atol=1e-7)

        cell_quality = mesh.cell_quality()
        np.testing.assert_allclose(bm.to_numpy(cell_quality), meshdata["cell_quality"], atol=1e-7)


if __name__ == "__main__":
    pytest.main(["./test_quadrangle_mesh.py", "-k", "test_init"])