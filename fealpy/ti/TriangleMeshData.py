#!/usr/bin/python3
'''!    	
	@Author: wpx
	@File Name: dict.py
	@Mail: wpx15673207315@gmail.com 
	@Created Time: 2022年04月12日 星期二 19时00分08秒
	@bref 
	@ref 
'''  
import numpy as np

phiphi11 = np.array(
        [[[1/6, 1/12, 1/12], [1/12, 1/6, 1/12], [1/12, 1/12, 1/6]]]) 

phiphi12 = np.array(
        [[[1/30, 2/15, 2/15, -1/60, 1/15, -1/60], [-1/60, 2/15, 1/15,
        1/30, 2/15, -1/60], [-1/60, 1/15, 2/15, -1/60, 2/15, 1/30]]])

phiphi13 = np.array(
        [[[1/60, 3/40, 3/40, 0, 3/20, 0, 1/120, 0, 0, 1/120], [1/120, 0,
        0, 3/40, 3/20, 0, 1/60, 3/40, 0, 1/120], [1/120, 0, 0, 0, 3/20, 3/40, 1/120, 0,
        3/40, 1/60]]])

phiphi21 = np.array(
        [[[1/30, -1/60, -1/60], [2/15, 2/15, 1/15], [2/15, 1/15, 2/15],
        [-1/60, 1/30, -1/60], [1/15, 2/15, 2/15], [-1/60, -1/60, 1/30]]])

phiphi22 = np.array(
        [[[1/30, 0, 0, -1/180, -1/45, -1/180], [0, 8/45, 4/45, 0, 4/45, -1/45], [0, 4/45,
        8/45, -1/45, 4/45, 0], [-1/180, 0, -1/45, 1/30, 0, -1/180], [-1/45, 4/45, 4/45,
        0, 8/45, 0], [-1/180, -1/45, 0, -1/180, 0, 1/30]]])

phiphi23 = np.array(
        [[[1/84, 9/280, 9/280, -3/140, -3/140, -3/140, 1/840, -1/140, -1/140, 1/840], [1/210,
        2/35, 1/35, 2/35, 6/35, -1/70, 1/210, 1/35, -1/70, 1/105], [1/210, 1/35, 2/35,
        -1/70, 6/35, 2/35, 1/105, -1/70, 1/35, 1/210], [1/840, -3/140, -1/140, 9/280,
        -3/140, -1/140, 1/84, 9/280, -3/140, 1/840], [1/105, -1/70, -1/70, 1/35,
        6/35, 1/35, 1/210, 2/35, 2/35, 1/210], [1/840, -1/140, -3/140,
        -1/140, -3/140, 9/280, 1/840, -3/140, 9/280, 1/84]]])

phiphi31 = np.array(
        [[[1/60, 1/120, 1/120], [3/40, 0, 0], [3/40, 0, 0], [0, 3/40, 0], [3/20, 3/20, 3/20],
        [0, 0, 3/40], [1/120, 1/60, 1/120], [0, 3/40, 0], [0, 0, 3/40], [1/120, 1/120,
        1/60]]])

phiphi32 = np.array(
        [[[1/30, 0, 0, -1/180, -1/45, -1/180], [0, 8/45, 4/45, 0, 4/45, -1/45], [0, 4/45,
        8/45, -1/45, 4/45, 0], [-1/180, 0, -1/45, 1/30, 0, -1/180], [-1/45, 4/45, 4/45,
        0, 8/45, 0], [-1/180, -1/45, 0, -1/180, 0, 1/30]]])

phiphi33 = np.array(
        [[[19/1680, 3/1120, 3/1120, 0, 3/560, 0, 11/6720, 9/2240,
        9/2240,11/6720], [3/1120, 9/112, 9/224, -9/320, 27/1120, -9/448, 0, -9/448,
        -9/1120, 9/2240], [3/1120, 9/224, 9/112, -9/448, 27/1120, -9/320, 9/2240,
        -9/1120, -9/448, 0], [0, -9/320, -9/448, 9/112, 27/1120, -9/1120, 3/1120,
        9/224, -9/448, 9/2240], [3/560, 27/1120, 27/1120, 27/1120, 81/280,
        27/1120, 3/560, 27/1120, 27/1120, 3/560], [0, -9/448, -9/320,
        -9/1120, 27/1120, 9/112, 9/2240, -9/448, 9/224, 3/1120],
        [11/6720, 0, 9/2240, 3/1120, 3/560, 9/2240, 19/1680, 3/1120, 0,
        11/6720], [9/2240, -9/448, -9/1120, 9/224, 27/1120, -9/448,
        3/1120, 9/112, -9/320, 0], [9/2240, -9/1120, -9/448,
        -9/448, 27/1120, 9/224, 0, -9/320, 9/112, 3/1120],
        [11/6720, 9/2240, 0, 9/2240, 3/560, 3/1120, 11/6720, 0,
        3/1120, 19/1680]]],dtype=np.float64)


phiphi = {'11':phiphi11, '12':phiphi12 ,'13':phiphi13,
          '21':phiphi21, '22':phiphi22 ,'23':phiphi23,
          '31':phiphi31, '32':phiphi32 ,'33':phiphi33}

gphigphi11 = np.array(
        [[[[1, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 1, 0], [0, 0, 0], [0,
        0, 0]], [[0, 0, 1], [0, 0, 0], [0, 0, 0]]], [[[0, 0, 0], [1, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 1], [0, 0, 0]]], [[[0,
        0, 0], [0, 0, 0], [1, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 1, 0]], [[0, 0,
        0], [0, 0, 0], [0, 0, 1]]]])

gphigphi12 = np.array(
        [[[[1/3, 0, 0], [0, 0, 0], [0, 0, 0]], [[4/3, 4/3, 0], [0, 0, 0], [0, 0, 0]],
        [[4/3, 0, 4/3], [0, 0, 0], [0, 0, 0]], [[0, 1/3, 0], [0, 0, 0], [0, 0,
        0]], [[0, 4/3, 4/3], [0, 0, 0], [0, 0, 0]], [[0, 0, 1/3], [0, 0, 0],
        [0, 0, 0]]], [[[0, 0, 0], [1/3, 0, 0], [0, 0, 0]], [[0, 0, 0],
        [4/3, 4/3, 0], [0, 0, 0]], [[0, 0, 0], [4/3, 0, 4/3], [0, 0,
        0]], [[0, 0, 0], [0, 1/3, 0], [0, 0, 0]], [[0, 0, 0], [0,
        4/3, 4/3], [0, 0, 0]], [[0, 0, 0], [0, 0, 1/3], [0,
        0, 0]]], [[[0, 0, 0], [0, 0, 0], [1/3, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [4/3, 4/3, 0]], [[0,
        0, 0], [0, 0, 0], [4/3, 0, 4/3]], [[0, 0,
        0], [0, 0, 0], [0, 1/3, 0]], [[0, 0,
        0], [0, 0, 0], [0, 4/3, 4/3]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 1/3]]]])

gphigphi21 = np.array(
        [[[[1/3, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 1/3, 0], [0, 0, 0],
        [0, 0, 0]], [[0, 0, 1/3], [0, 0, 0], [0, 0, 0]]], [[[4/3, 0, 0], [4/3, 0, 0], [0,
        0, 0]], [[0, 4/3, 0], [0, 4/3, 0], [0, 0, 0]], [[0, 0, 4/3], [0, 0, 4/3], [0,
        0, 0]]], [[[4/3, 0, 0], [0, 0, 0], [4/3, 0, 0]], [[0, 4/3, 0], [0, 0, 0],
        [0, 4/3, 0]], [[0, 0, 4/3], [0, 0, 0], [0, 0, 4/3]]], [[[0, 0, 0],
        [1/3, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 1/3, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 1/3], [0, 0, 0]]], [[[0, 0, 0], [4/3, 0, 0],
        [4/3, 0, 0]], [[0, 0, 0], [0, 4/3, 0], [0, 4/3, 0]], [[0, 0,
        0], [0, 0, 4/3], [0, 0, 4/3]]], [[[0, 0, 0], [0, 0, 0],
        [1/3, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 1/3, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 1/3]]]])

gphigphi22 = np.array([[[[1, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 4/3, 0], [0, 0, 0], [0,
        0, 0]], [[0, 0, 4/3], [0, 0, 0], [0, 0, 0]], [[0, -1/3, 0], [0, 0, 0], [0, 0,0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, -1/3], [0, 0, 0], [0, 0, 0]]], [[[0,
        0, 0], [4/3, 0, 0], [0, 0, 0]], [[8/3, 4/3, 0], [4/3, 8/3, 0], [0, 0, 0]],
        [[4/3, 0, 4/3], [4/3, 0, 8/3], [0, 0, 0]], [[0, 4/3, 0], [0, 0, 0], [0, 0,
        0]], [[0, 4/3, 8/3], [0, 4/3, 4/3], [0, 0, 0]], [[0, 0, 0], [0, 0, 0],
        [0, 0, 0]]], [[[0, 0, 0], [0, 0, 0], [4/3, 0, 0]], [[4/3, 4/3, 0],
        [0, 0, 0], [4/3, 8/3, 0]], [[8/3, 0, 4/3], [0, 0, 0], [4/3, 0,
        8/3]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 8/3, 4/3], [0, 0, 0], [0, 4/3,
        4/3]], [[0, 0, 4/3], [0, 0, 0], [0, 0, 0]]], [[[0, 0, 0], [-1/3, 0, 0],
        [0, 0, 0]], [[0, 0, 0], [4/3, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0,
        0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0],
        [0, 0, 4/3], [0, 0, 0]], [[0, 0, 0], [0, 0, -1/3], [0, 0,
        0]]], [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0],
        [4/3, 4/3, 0], [8/3, 4/3, 0]], [[0, 0, 0], [8/3, 0,
        4/3], [4/3, 0, 4/3]], [[0, 0, 0], [0, 0, 0], [0,
        4/3, 0]], [[0, 0, 0], [0, 8/3, 4/3], [0, 4/3,
        8/3]], [[0, 0, 0], [0, 0, 4/3], [0, 0, 0]]], [[[0, 0, 0], [0, 0, 0], [-1/3,
        0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [4/3,
        0, 0]], [[0, 0, 0], [0, 0, 0], [0, -1/3, 0]], [[0, 0, 0], [0, 0, 0],
        [0, 4/3, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 1]]]])

gphigphi = {'11':gphigphi11, '12':gphigphi12, 
            '21':gphigphi22, '22':gphigphi22}

gphiphi11 = np.array(
        [[[1/3, 0, 0], [1/3, 0, 0], [1/3, 0, 0]], [[0, 1/3, 0], [0, 1/3,
        0], [0, 1/3, 0]], [[0, 0, 1/3], [0, 0, 1/3], [0, 0, 1/3]]]) 

gphiphi12 = np.array(
        [[[0, 0, 0], [1/3, 0, 0], [1/3, 0, 0], [0, 0, 0], [1/3, 0, 0],
        [0, 0, 0]], [[0, 0, 0], [0, 1/3, 0], [0, 1/3, 0], [0, 0, 0], [0, 1/3, 0], [0, 0,
        0]], [[0, 0, 0], [0, 0, 1/3], [0, 0, 1/3], [0, 0, 0], [0, 0, 1/3], [0, 0, 0]]])

gphiphi21 = np.array(
        [[[1/3, 0, 0], [0, 0, 0], [0, 0, 0]], [[1/3, 2/3, 0], [2/3, 1/3,
        0], [1/3, 1/3, 0]], [[1/3, 0, 2/3], [1/3, 0, 1/3], [2/3, 0, 1/3]], [[0, 0, 0],
        [0, 1/3, 0], [0, 0, 0]], [[0, 1/3, 1/3], [0, 1/3, 2/3], [0, 2/3, 1/3]], [[0,
        0, 0], [0, 0, 0], [0, 0, 1/3]]])

gphiphi22 = np.array(
        [[[2/15, 0, 0], [1/5, 0, 0], [1/5, 0, 0], [-1/15, 0, 0], [-1/15,
        0, 0], [-1/15, 0, 0]], [[-1/15, 2/15, 0], [8/15, 8/15, 0], [4/15, 8/15, 0],
        [2/15, -1/15, 0], [8/15, 4/15, 0], [-1/15, -1/15, 0]], [[-1/15, 0, 2/15],
        [4/15, 0, 8/15], [8/15, 0, 8/15], [-1/15, 0, -1/15], [8/15, 0, 4/15],
        [2/15, 0, -1/15]], [[0, -1/15, 0], [0, 1/5, 0], [0, -1/15, 0], [0, 2/15,
        0], [0, 1/5, 0], [0, -1/15, 0]], [[0, -1/15, -1/15], [0, 4/15, 8/15],
        [0, 8/15, 4/15], [0, -1/15, 2/15], [0, 8/15, 8/15], [0, 2/15,
        -1/15]], [[0, 0, -1/15], [0, 0, -1/15], [0, 0, 1/5], [0, 0,
        -1/15], [0, 0, 1/5], [0, 0, 2/15]]])

gphiphi = {'11':gphiphi11, '12':gphiphi12, 
           '21':gphiphi21, '22':gphiphi22}