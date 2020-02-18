from draw3d import *
from vectors import dot, component

def drawOctaEdges():
    top = (0, 0, 1)
    bottom = (0, 0, -1)
    xy_plane = [(1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0)]

    edges = [Segment3D(top, p) for p in xy_plane] +\
        [Segment3D(bottom, p) for p in xy_plane] +\
        [Segment3D(xy_plane[i], xy_plane[(i+1) % 4]) for i in range(0, 4)]

    draw3d(*edges)
    

faces = [
    [(1, 0, 0), (0, 1, 0), (0, 0, 1)],
    [(1, 0, 0), (0, 0, -1), (0, 1, 0)],
    [(1, 0, 0), (0, 0, 1), (0, -1, 0)],
    [(1, 0, 0), (0, -1, 0), (0, 0, -1)],
    [(-1 ,0 ,0), (0, 0, 1), (0, 1, 0)],
    [(-1, 0, 0), (0, 1, 0), (0, 0, -1)],
    [(-1, 0, 0), (0, -1, 0), (0, 0, 1)],
    [(-1, 0, 0), (0, 0, -1), (0, -1, 0)],
]

def getVertices(faces):
    return list(set([vertex for face in faces for vertex in face]))


def vector_to_2d(vector):
    XOY = {'x': (1,0,0), 'y': (0,1,0)}
    
    return (component(vector, XOY['x']), component(vector, XOY['y']))


def face_to_2d(face):
    return [vector_to_2d(vertex) for vertex in face]


