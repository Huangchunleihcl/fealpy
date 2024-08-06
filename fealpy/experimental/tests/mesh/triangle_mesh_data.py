import numpy as np

# 定义多个典型的 TriangleMesh 对象
init_data = [
    {
        "node": np.array([[0, 0], [1, 0], [0, 1]], dtype=np.float64),
        "edge": np.array([[0, 1], [2, 0], [1, 2]], dtype=np.int32), 
        "cell": np.array([[0, 1, 2]], dtype=np.int32),
        "face2cell": np.array([[0, 0, 2, 2], [0, 0, 1, 1], [0, 0, 0, 0]], dtype=np.int32),
        "NN": 3,
        "NE": 3,
        "NF": 3,
        "NC": 1
    },
    {
        "node": np.array([[0, 0], [1, 0], [1, 1], [0, 1]], dtype=np.float64),
        "edge": np.array([[0, 1], [2, 0], [3, 0], [1, 2], [2, 3]], dtype=np.int32),
        "cell": np.array([[1, 2, 0], [3, 0, 2]], dtype=np.int32),
        "face2cell": np.array([[0, 0, 1, 1], [0, 1, 0, 0], [1, 1, 2, 2], [0, 0, 2, 2],[1, 1, 1, 1]], dtype=np.int32),
        "NN": 4,
        "NE": 5, 
        "NF": 5,
        "NC": 2
    }
]

from_one_triangle_data = [
        {
            "node": np.array([[0.       , 0.       ], [1.       , 0.       ],[0.5      , 0.8660254]], dtype=np.float64),
            "edge": np.array([[0, 1], [2, 0], [1, 2]], dtype=np.int32),
            "cell": np.array([[0, 1, 2]], dtype=np.int32),
            "face2cell": np.array([[0, 0, 2, 2],[0, 0, 1, 1],[0, 0, 0, 0]], dtype=np.int32),
            "NN": 3,
            "NE": 3,
            "NF": 3,
            "NC": 1
            }
]

from_box_data= [
            {
                "node": np.array([[0 , 0], [0, 0.5], [0, 1], [0.5, 0], 
                    [0.5, 0.5], [0.5, 1], [1, 0], [1, 0.5], [1, 1]], dtype=np.float64),
                "edge": np.array([[1, 0], [0, 3], [4, 0], [2, 1], [1, 4], [5, 1], 
                    [5, 2], [3, 4], [3, 6], [7, 3], [4, 5], [4, 7], [8, 4], [8, 5], 
                    [6, 7], [7, 8]], dtype=np.int32), 
                "cell": np.array([[3, 4, 0], [6, 7, 3], [4, 5, 1], [7, 8, 4], 
                    [1, 0, 4], [4, 3, 7], [2, 1, 5], [5, 4, 8]], dtype=np.int32),
                "face2cell": np.array([[4, 4, 2, 2], [0, 0, 1, 1], [0, 4, 0, 0], [6, 6, 2, 2],
                    [2, 4, 1, 1], [2, 6, 0, 0], [6, 6, 1, 1], [0, 5, 2, 2], [1, 1, 1, 1], 
                    [1, 5, 0, 0], [2, 7, 2, 2], [3, 5, 1, 1], [3, 7, 0, 0], [7, 7, 1, 1], 
                    [1, 1, 2, 2], [3, 3, 2, 2]], dtype=np.int32),
                "NN": 9,
                "NE": 16,
                "NF": 16,
                "NC": 8
            }
]

entity_measure_data = [
        {
            "node_measure": np.array([0.0], dtype=np.float64),
            "edge_measure": np.array([1.0, 1.0, np.sqrt(2)], dtype=np.float64),
            "cell_measure": np.array([0.5], dtype=np.float64)
            }
]

grad_lambda_data = [
        {
            "val": np.array([[[ 1., -1.],
            [ 0.,  1.],
            [-1.,  0.]],

           [[ 1., -1.],
            [ 0.,  1.],
            [-1.,  0.]],

           [[ 1., -1.],
            [ 0.,  1.],
            [-1.,  0.]],

           [[ 1., -1.],
            [ 0.,  1.],
            [-1.,  0.]],

           [[-1.,  1.],
            [ 0., -1.],
            [ 1.,  0.]],

           [[-1.,  1.],
            [ 0., -1.],
            [ 1.,  0.]],

           [[-1.,  1.],
            [ 0., -1.],
            [ 1.,  0.]],

           [[-1.,  1.],
            [ 0., -1.],
            [ 1.,  0.]]], dtype=np.float64)
       }
]

grad_shape_function_data = [
        {
            "gphi": np.array([[[[ 4.53478058, -4.53478058],
             [ 0.73260971,  5.80217088],
             [-5.80217088, -0.73260971],
             [ 0.        , -1.26739029],
             [-0.73260971,  0.73260971],
             [ 1.26739029,  0.        ]],

            [[ 4.53478058, -4.53478058],
             [ 0.73260971,  5.80217088],
             [-5.80217088, -0.73260971],
             [ 0.        , -1.26739029],
             [-0.73260971,  0.73260971],
             [ 1.26739029,  0.        ]],

            [[ 4.53478058, -4.53478058],
             [ 0.73260971,  5.80217088],
             [-5.80217088, -0.73260971],
             [ 0.        , -1.26739029],
             [-0.73260971,  0.73260971],
             [ 1.26739029,  0.        ]],

            [[ 4.53478058, -4.53478058],
             [ 0.73260971,  5.80217088],
             [-5.80217088, -0.73260971],
             [ 0.        , -1.26739029],
             [-0.73260971,  0.73260971],
             [ 1.26739029,  0.        ]],

            [[-4.53478058,  4.53478058],
             [-0.73260971, -5.80217088],
             [ 5.80217088,  0.73260971],
             [ 0.        ,  1.26739029],
             [ 0.73260971, -0.73260971],
             [-1.26739029,  0.        ]],

            [[-4.53478058,  4.53478058],
             [-0.73260971, -5.80217088],
             [ 5.80217088,  0.73260971],
             [ 0.        ,  1.26739029],
             [ 0.73260971, -0.73260971],
             [-1.26739029,  0.        ]],

            [[-4.53478058,  4.53478058],
             [-0.73260971, -5.80217088],
             [ 5.80217088,  0.73260971],
             [ 0.        ,  1.26739029],
             [ 0.73260971, -0.73260971],
             [-1.26739029,  0.        ]],

            [[-4.53478058,  4.53478058],
             [-0.73260971, -5.80217088],
             [ 5.80217088,  0.73260971],
             [ 0.        ,  1.26739029],
             [ 0.73260971, -0.73260971],
             [-1.26739029,  0.        ]]],


           [[[-1.26739029,  1.26739029],
             [ 6.53478058, -5.80217088],
             [ 0.        , -0.73260971],
             [ 0.        ,  4.53478058],
             [-6.53478058,  0.73260971],
             [ 1.26739029,  0.        ]],

            [[-1.26739029,  1.26739029],
             [ 6.53478058, -5.80217088],
             [ 0.        , -0.73260971],
             [ 0.        ,  4.53478058],
             [-6.53478058,  0.73260971],
             [ 1.26739029,  0.        ]],

            [[-1.26739029,  1.26739029],
             [ 6.53478058, -5.80217088],
             [ 0.        , -0.73260971],
             [ 0.        ,  4.53478058],
             [-6.53478058,  0.73260971],
             [ 1.26739029,  0.        ]],

            [[-1.26739029,  1.26739029],
             [ 6.53478058, -5.80217088],
             [ 0.        , -0.73260971],
             [ 0.        ,  4.53478058],
             [-6.53478058,  0.73260971],
             [ 1.26739029,  0.        ]],

            [[ 1.26739029, -1.26739029],
             [-6.53478058,  5.80217088],
             [ 0.        ,  0.73260971],
             [ 0.        , -4.53478058],
             [ 6.53478058, -0.73260971],
             [-1.26739029,  0.        ]],

            [[ 1.26739029, -1.26739029],
             [-6.53478058,  5.80217088],
             [ 0.        ,  0.73260971],
             [ 0.        , -4.53478058],
             [ 6.53478058, -0.73260971],
             [-1.26739029,  0.        ]],

            [[ 1.26739029, -1.26739029],
             [-6.53478058,  5.80217088],
             [ 0.        ,  0.73260971],
             [ 0.        , -4.53478058],
             [ 6.53478058, -0.73260971],
             [-1.26739029,  0.        ]],

            [[ 1.26739029, -1.26739029],
             [-6.53478058,  5.80217088],
             [ 0.        ,  0.73260971],
             [ 0.        , -4.53478058],
             [ 6.53478058, -0.73260971],
             [-1.26739029,  0.        ]]],


           [[[-1.26739029,  1.26739029],
             [ 0.73260971,  0.        ],
             [ 5.80217088, -6.53478058],
             [ 0.        , -1.26739029],
             [-0.73260971,  6.53478058],
             [-4.53478058,  0.        ]],

            [[-1.26739029,  1.26739029],
             [ 0.73260971,  0.        ],
             [ 5.80217088, -6.53478058],
             [ 0.        , -1.26739029],
             [-0.73260971,  6.53478058],
             [-4.53478058,  0.        ]],

            [[-1.26739029,  1.26739029],
             [ 0.73260971,  0.        ],
             [ 5.80217088, -6.53478058],
             [ 0.        , -1.26739029],
             [-0.73260971,  6.53478058],
             [-4.53478058,  0.        ]],

            [[-1.26739029,  1.26739029],
             [ 0.73260971,  0.        ],
             [ 5.80217088, -6.53478058],
             [ 0.        , -1.26739029],
             [-0.73260971,  6.53478058],
             [-4.53478058,  0.        ]],

            [[ 1.26739029, -1.26739029],
             [-0.73260971,  0.        ],
             [-5.80217088,  6.53478058],
             [ 0.        ,  1.26739029],
             [ 0.73260971, -6.53478058],
             [ 4.53478058,  0.        ]],

            [[ 1.26739029, -1.26739029],
             [-0.73260971,  0.        ],
             [-5.80217088,  6.53478058],
             [ 0.        ,  1.26739029],
             [ 0.73260971, -6.53478058],
             [ 4.53478058,  0.        ]],

            [[ 1.26739029, -1.26739029],
             [-0.73260971,  0.        ],
             [-5.80217088,  6.53478058],
             [ 0.        ,  1.26739029],
             [ 0.73260971, -6.53478058],
             [ 4.53478058,  0.        ]],

            [[ 1.26739029, -1.26739029],
             [-0.73260971,  0.        ],
             [-5.80217088,  6.53478058],
             [ 0.        ,  1.26739029],
             [ 0.73260971, -6.53478058],
             [ 4.53478058,  0.        ]]],


           [[[ 1.56758793, -1.56758793],
             [ 3.56758793,  0.        ],
             [-2.70276378, -0.86482415],
             [ 0.        ,  1.56758793],
             [-3.56758793,  0.86482415],
             [ 1.13517585,  0.        ]],

            [[ 1.56758793, -1.56758793],
             [ 3.56758793,  0.        ],
             [-2.70276378, -0.86482415],
             [ 0.        ,  1.56758793],
             [-3.56758793,  0.86482415],
             [ 1.13517585,  0.        ]],

            [[ 1.56758793, -1.56758793],
             [ 3.56758793,  0.        ],
             [-2.70276378, -0.86482415],
             [ 0.        ,  1.56758793],
             [-3.56758793,  0.86482415],
             [ 1.13517585,  0.        ]],

            [[ 1.56758793, -1.56758793],
             [ 3.56758793,  0.        ],
             [-2.70276378, -0.86482415],
             [ 0.        ,  1.56758793],
             [-3.56758793,  0.86482415],
             [ 1.13517585,  0.        ]],

            [[-1.56758793,  1.56758793],
             [-3.56758793,  0.        ],
             [ 2.70276378,  0.86482415],
             [ 0.        , -1.56758793],
             [ 3.56758793, -0.86482415],
             [-1.13517585,  0.        ]],

            [[-1.56758793,  1.56758793],
             [-3.56758793,  0.        ],
             [ 2.70276378,  0.86482415],
             [ 0.        , -1.56758793],
             [ 3.56758793, -0.86482415],
             [-1.13517585,  0.        ]],

            [[-1.56758793,  1.56758793],
             [-3.56758793,  0.        ],
             [ 2.70276378,  0.86482415],
             [ 0.        , -1.56758793],
             [ 3.56758793, -0.86482415],
             [-1.13517585,  0.        ]],

            [[-1.56758793,  1.56758793],
             [-3.56758793,  0.        ],
             [ 2.70276378,  0.86482415],
             [ 0.        , -1.56758793],
             [ 3.56758793, -0.86482415],
             [-1.13517585,  0.        ]]],


           [[[ 1.56758793, -1.56758793],
             [ 0.86482415,  2.70276378],
             [ 0.        , -3.56758793],
             [ 0.        , -1.13517585],
             [-0.86482415,  3.56758793],
             [-1.56758793,  0.        ]],

            [[ 1.56758793, -1.56758793],
             [ 0.86482415,  2.70276378],
             [ 0.        , -3.56758793],
             [ 0.        , -1.13517585],
             [-0.86482415,  3.56758793],
             [-1.56758793,  0.        ]],

            [[ 1.56758793, -1.56758793],
             [ 0.86482415,  2.70276378],
             [ 0.        , -3.56758793],
             [ 0.        , -1.13517585],
             [-0.86482415,  3.56758793],
             [-1.56758793,  0.        ]],

            [[ 1.56758793, -1.56758793],
             [ 0.86482415,  2.70276378],
             [ 0.        , -3.56758793],
             [ 0.        , -1.13517585],
             [-0.86482415,  3.56758793],
             [-1.56758793,  0.        ]],

            [[-1.56758793,  1.56758793],
             [-0.86482415, -2.70276378],
             [ 0.        ,  3.56758793],
             [ 0.        ,  1.13517585],
             [ 0.86482415, -3.56758793],
             [ 1.56758793,  0.        ]],

            [[-1.56758793,  1.56758793],
             [-0.86482415, -2.70276378],
             [ 0.        ,  3.56758793],
             [ 0.        ,  1.13517585],
             [ 0.86482415, -3.56758793],
             [ 1.56758793,  0.        ]],

            [[-1.56758793,  1.56758793],
             [-0.86482415, -2.70276378],
             [ 0.        ,  3.56758793],
             [ 0.        ,  1.13517585],
             [ 0.86482415, -3.56758793],
             [ 1.56758793,  0.        ]],

            [[-1.56758793,  1.56758793],
             [-0.86482415, -2.70276378],
             [ 0.        ,  3.56758793],
             [ 0.        ,  1.13517585],
             [ 0.86482415, -3.56758793],
             [ 1.56758793,  0.        ]]],


           [[[-1.13517585,  1.13517585],
             [ 3.56758793, -2.70276378],
             [ 2.70276378, -3.56758793],
             [ 0.        ,  1.56758793],
             [-3.56758793,  3.56758793],
             [-1.56758793,  0.        ]],

            [[-1.13517585,  1.13517585],
             [ 3.56758793, -2.70276378],
             [ 2.70276378, -3.56758793],
             [ 0.        ,  1.56758793],
             [-3.56758793,  3.56758793],
             [-1.56758793,  0.        ]],

            [[-1.13517585,  1.13517585],
             [ 3.56758793, -2.70276378],
             [ 2.70276378, -3.56758793],
             [ 0.        ,  1.56758793],
             [-3.56758793,  3.56758793],
             [-1.56758793,  0.        ]],

            [[-1.13517585,  1.13517585],
             [ 3.56758793, -2.70276378],
             [ 2.70276378, -3.56758793],
             [ 0.        ,  1.56758793],
             [-3.56758793,  3.56758793],
             [-1.56758793,  0.        ]],

            [[ 1.13517585, -1.13517585],
             [-3.56758793,  2.70276378],
             [-2.70276378,  3.56758793],
             [ 0.        , -1.56758793],
             [ 3.56758793, -3.56758793],
             [ 1.56758793,  0.        ]],

            [[ 1.13517585, -1.13517585],
             [-3.56758793,  2.70276378],
             [-2.70276378,  3.56758793],
             [ 0.        , -1.56758793],
             [ 3.56758793, -3.56758793],
             [ 1.56758793,  0.        ]],

            [[ 1.13517585, -1.13517585],
             [-3.56758793,  2.70276378],
             [-2.70276378,  3.56758793],
             [ 0.        , -1.56758793],
             [ 3.56758793, -3.56758793],
             [ 1.56758793,  0.        ]],

            [[ 1.13517585, -1.13517585],
             [-3.56758793,  2.70276378],
             [-2.70276378,  3.56758793],
             [ 0.        , -1.56758793],
             [ 3.56758793, -3.56758793],
             [ 1.56758793,  0.        ]]]], dtype=np.float64)
            }
]

interpolation_point_data = [
        {
            "ips": np.array([[0.   , 0.   ], [0.   , 0.5  ], [0.   , 1.   ], 
                [0.5  , 0.   ], [0.5  , 0.5  ], [0.5  , 1.   ],
                [1.   , 0.   ], [1.   , 0.5  ], [1.   , 1.   ],
                [0.   , 0.375], [0.   , 0.25 ], [0.   , 0.125],
                [0.125, 0.   ], [0.25 , 0.   ], [0.375, 0.   ],
                [0.375, 0.375], [0.25 , 0.25 ], [0.125, 0.125],
                [0.   , 0.875], [0.   , 0.75 ], [0.   , 0.625],
                [0.125, 0.5  ], [0.25 , 0.5  ], [0.375, 0.5  ],
                [0.375, 0.875], [0.25 , 0.75 ], [0.125, 0.625],
                [0.375, 1.   ], [0.25 , 1.   ], [0.125, 1.   ],
                [0.5  , 0.125], [0.5  , 0.25 ], [0.5  , 0.375],
                [0.625, 0.   ], [0.75 , 0.   ], [0.875, 0.   ],
                [0.875, 0.375], [0.75 , 0.25 ], [0.625, 0.125],
                [0.5  , 0.625], [0.5  , 0.75 ], [0.5  , 0.875],
                [0.625, 0.5  ], [0.75 , 0.5  ], [0.875, 0.5  ],
                [0.875, 0.875], [0.75 , 0.75 ], [0.625, 0.625],
                [0.875, 1.   ], [0.75 , 1.   ], [0.625, 1.   ],
                [1.   , 0.125], [1.   , 0.25 ], [1.   , 0.375],
                [1.   , 0.625], [1.   , 0.75 ], [1.   , 0.875],
                [0.375, 0.125], [0.375, 0.25 ], [0.25 , 0.125],
                [0.875, 0.125], [0.875, 0.25 ], [0.75 , 0.125],
                [0.375, 0.625], [0.375, 0.75 ], [0.25 , 0.625],
                [0.875, 0.625], [0.875, 0.75 ], [0.75 , 0.625],
                [0.125, 0.375], [0.125, 0.25 ], [0.25 , 0.375],
                [0.625, 0.375], [0.625, 0.25 ], [0.75 , 0.375],
                [0.125, 0.875], [0.125, 0.75 ], [0.25 , 0.875],
                [0.625, 0.875], [0.625, 0.75 ], [0.75 , 0.875]], dtype=np.float64),
            "cip": np.array([[ 3, 30, 14, 31, 57, 13, 32, 58, 59, 12,  4, 15, 16, 17,  0],
                [ 6, 51, 35, 52, 60, 34, 53, 61, 62, 33,  7, 36, 37, 38,  3],
                [ 4, 39, 23, 40, 63, 22, 41, 64, 65, 21,  5, 24, 25, 26,  1],
                [ 7, 54, 44, 55, 66, 43, 56, 67, 68, 42,  8, 45, 46, 47,  4],
                [ 1,  9, 21, 10, 69, 22, 11, 70, 71, 23,  0, 17, 16, 15,  4],
                [ 4, 32, 42, 31, 72, 43, 30, 73, 74, 44,  3, 38, 37, 36,  7],
                [ 2, 18, 29, 19, 75, 28, 20, 76, 77, 27,  1, 26, 25, 24,  5],
                [ 5, 41, 50, 40, 78, 49, 39, 79, 80, 48,  4, 47, 46, 45,  8]], dtype=np.int32),
            "fip": np.array([[ 1,  9, 10, 11,  0], [ 0, 12, 13, 14,  3], 
                [ 4, 15, 16, 17,  0], [ 2, 18, 19, 20,  1],
                [ 1, 21, 22, 23,  4], [ 5, 24, 25, 26,  1],
                [ 5, 27, 28, 29,  2], [ 3, 30, 31, 32,  4],
                [ 3, 33, 34, 35,  6], [ 7, 36, 37, 38,  3],
                [ 4, 39, 40, 41,  5], [ 4, 42, 43, 44,  7],
                [ 8, 45, 46, 47,  4], [ 8, 48, 49, 50,  5],
                [ 6, 51, 52, 53,  7], [ 7, 54, 55, 56,  8]], dtype=np.int32)
            }
] 

uniform_refine_data = [
        {
            "node": np.array([[0.  , 0.  ], [1.  , 0.  ], [0.  , 1.  ],
                [0.5 , 0.  ], [0.  , 0.5 ], [0.5 , 0.5 ], [0.25, 0.  ],
                [0.  , 0.25], [0.75, 0.  ], [0.75, 0.25], [0.  , 0.75],
                [0.25, 0.75], [0.25, 0.25], [0.5 , 0.25], [0.25, 0.5 ]], dtype=np.float64),
            "cell": np.array([[ 0,  6,  7], [ 3,  8, 13], [ 4, 14, 10],
                [ 5, 14, 13], [ 6,  3, 12], [ 8,  1,  9], [14,  5, 11], [14,  4, 12],
                [ 7, 12,  4], [13,  9,  5], [10, 11,  2], [13, 12,  3],
                [12,  7,  6], [ 9, 13,  8], [11, 10, 14], [12, 13, 14]], dtype=np.int32),
            "face2cell": np.array([[ 0,  0,  2,  2], [ 0,  0,  1,  1], [ 5,  5,  2,  2],
                [ 5,  5,  0,  0], [10, 10,  1,  1], [10, 10,  0,  0], [ 4,  4,  2,  2], 
                [ 1,  1,  2,  2], [ 4, 11,  0,  0], [ 1, 11,  1,  1], [ 8,  8,  1,  1], 
                [ 2,  2,  1,  1], [ 7,  8,  0,  0], [ 2,  7,  2,  2], [ 9,  9,  0,  0],
                [ 6,  6,  0,  0], [ 3,  9,  1,  1], [ 3,  6,  2,  2], [ 0, 12,  0,  0],
                [ 4, 12,  1,  1], [ 8, 12,  2,  2], [ 5, 13,  1,  1], [ 1, 13,  0,  0],
                [ 9, 13,  2,  2], [10, 14,  2,  2], [ 2, 14,  0,  0], [ 6, 14,  1,  1],
                [11, 15,  2,  2], [ 7, 15,  1,  1], [ 3, 15,  0,  0]], dtype=np.int32),
            "cell2edge": np.array([[18,  1,  0], [22,  9,  7], [25, 11, 13],
                [29, 16, 17], [ 8, 19,  6], [ 3, 21,  2], [15, 26, 17], 
                [12, 28, 13], [12, 10, 20], [14, 16, 23], [ 5,  4, 24], [ 8,  9, 27],
                [18, 19, 20], [22, 21, 23], [25, 26, 24], [29, 28, 27]], dtype=np.int32)
            }
]

jacobian_matrix_data = [
        {"jacobian_matrix": 
        np.array([[[ 0. , -0.5],
        [ 0.5,  0. ]],

       [[ 0. , -0.5],
        [ 0.5,  0. ]],

       [[ 0. , -0.5],
        [ 0.5,  0. ]],

       [[ 0. , -0.5],
        [ 0.5,  0. ]],

       [[ 0. ,  0.5],
        [-0.5,  0. ]],

       [[ 0. ,  0.5],
        [-0.5,  0. ]],

       [[ 0. ,  0.5],
        [-0.5,  0. ]],

       [[ 0. ,  0.5],
        [-0.5,  0. ]]], dtype=np.float64)
            }
]

from_unit_sphere_surface_data= [
            {
                "node": np.array([[ 0.        ,  0.85065081,  0.52573111],
                   [ 0.        ,  0.85065081, -0.52573111],
                   [ 0.85065081,  0.52573111,  0.        ],
                   [ 0.85065081, -0.52573111,  0.        ],
                   [ 0.        , -0.85065081, -0.52573111],
                   [ 0.        , -0.85065081,  0.52573111],
                   [ 0.52573111,  0.        ,  0.85065081],
                   [-0.52573111,  0.        ,  0.85065081],
                   [ 0.52573111,  0.        , -0.85065081],
                   [-0.52573111,  0.        , -0.85065081],
                   [-0.85065081,  0.52573111,  0.        ],
                   [-0.85065081, -0.52573111,  0.        ]], dtype=np.float64),
                "edge": np.array([[ 1,  0], [ 2,  0], [ 0,  6], [ 0,  7], [10,  0],
                   [ 1,  2], [ 8,  1], [ 1,  9], [ 1, 10], [ 3,  2], [ 6,  2],
                   [ 8,  2], [ 3,  4], [ 5,  3], [ 6,  3],  [3,  8], [ 5,  4],
                   [ 4,  8], [ 9,  4], [11,  4], [ 6,  5], [ 7,  5], [ 5, 11],
                   [ 6,  7], [ 7, 10], [11,  7], [ 8,  9], [ 9, 10], [11,  9], [10, 11]], dtype=np.int32),
                "cell": np.array([[ 6,  2,  0], [ 3,  2,  6], [ 5,  3,  6],
                   [ 5,  6,  7], [ 6,  0,  7], [ 3,  8,  2], [ 2,  8,  1], 
                   [ 2,  1,  0], [ 0,  1, 10], [ 1,  9, 10], [ 8,  9,  1], 
                   [ 4,  8,  3], [ 4,  3,  5], [ 4,  5, 11], [ 7, 10, 11],
                   [ 0, 10,  7], [ 4, 11,  9], [ 8,  4,  9], [ 5,  7, 11], 
                   [10,  9, 11]], dtype=np.int32),
                "face2cell": np.array([[ 7,  8,  0,  2],
                   [ 0,  7,  0,  1],
                   [ 0,  4,  1,  2],
                   [ 4, 15,  0,  1],
                   [ 8, 15,  1,  2],
                   [ 6,  7,  1,  2],
                   [ 6, 10,  0,  1],
                   [ 9, 10,  2,  0],
                   [ 8,  9,  0,  1],
                   [ 1,  5,  2,  1],
                   [ 0,  1,  2,  0],
                   [ 5,  6,  0,  2],
                   [11, 12,  1,  2],
                   [ 2, 12,  2,  0],
                   [ 1,  2,  1,  0],
                   [ 5, 11,  2,  0],
                   [12, 13,  1,  2],
                   [11, 17,  2,  2],
                   [16, 17,  1,  0],
                   [13, 16,  1,  2],
                   [ 2,  3,  1,  2],
                   [ 3, 18,  1,  2],
                   [13, 18,  0,  1],
                   [ 3,  4,  0,  1],
                   [14, 15,  2,  0],
                   [14, 18,  1,  0],
                   [10, 17,  2,  1],
                   [ 9, 19,  0,  2],
                   [16, 19,  0,  0],
                   [14, 19,  0,  1]], dtype=np.int32),
                "NN": 12,
                "NE": 30,
                "NF": 30,
                "NC": 20
            }
]
