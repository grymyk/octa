import random
import math
import transformations as tf

import sys

from matrix import *

alpha, beta, gamma = 0.123, -1.234, 2.345
origin, xaxis, yaxis, zaxis = [0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]

Ry = tf.rotation_matrix(beta, yaxis)

def translate(vertices, vector_tl = (1, 1, 1)):
    gomo_ver = gomoCoord(vertices)
    
    matrix_tl = translation_matrix(vector_tl)
    sys.getsizeof(matrix_tl)
    
    v1 = []
    
    for vertex in gomo_ver:        
        v = multiply_matrix_vector(matrix_tl, vertex)
        v1.append(v)

    return euclidCoord(v1)
    

def archimedean_spiral(t):
    coord = []
    
    angle = math.pi / 4 * t
    
    v = -2.4
    c = 0.5
    
    x = (v * t + c) * math.cos(angle)
    y = (v * t + c) * math.sin(angle)
    z = 0
    
    coord.append(x)
    coord.append(y)
    coord.append(z)
    
    return coord

def coors_random():
    max_distance = 100
    coord = []
    
    coord.append(random.randrange(-10, 10))
    coord.append(random.randrange(-10, 10))
    coord.append(random.randrange(-1 * max_distance, -20) )

    return coord

