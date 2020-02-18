from OpenGL.GL import *

import random

cubeVertices = (
    (1, 1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1),
    (1, 1, -1), (1, -1, -1), (-1, -1, -1), (-1, 1, -1)
)

cubeEdges = (
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (7, 6), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
)

cubeQuads = (
    (0, 3, 6, 4), (2, 5, 6, 3), (1, 2, 5, 7),
    (1, 0, 4, 7), (7, 4, 6, 5), (2, 3, 0, 1)
)

def Cube(vertices):
    print(vertices)
    
    # solidCube
    # ~ glBegin(GL_QUADS)
    # ~ for surface in cubeFaces:
        # ~ x = 0

        # ~ for vertex in surface:
            # ~ x += 1

            # ~ glColor3fv(colors[x])
            # ~ glVertex3fv(cubeVertices[vertex])
    # ~ glEnd()
    
    # wireCube
    
    print('Cube')
    
    glBegin(GL_LINES)
    for edge in cubeEdges:
        for vertex in edge:
            print(vertex)
            print(vertices)
            glVertex3fv(vertices[vertex])
    glEnd()


def set_vertices(max_distance):
    x_coord = 2
    y_coord = 7
    z_coord = 2

    vertices_new = []

    for vert in cubeVertices:
        vert_new = []

        x_new = vert[0] + x_coord
        y_new = vert[1] + y_coord
        z_new = vert[2] + z_coord

        vert_new.append(x_new)
        vert_new.append(y_new)
        vert_new.append(z_new)

        vertices_new.append(vert_new)

    return vertices_new

def getCubes(number):
    max_distance = 1
    cubes = []

    # ~ for x in range(number):
        # ~ print(x)
        
    cubes.append( set_vertices(max_distance ))

    return cubes
 
def drawCubes(cubes):
    number_cube = 1

    cubes = getCubes(number_cube)
    print(cubes)
    
    for cube in cubes:
        Cube(cubes[cube])


def wireCube(dict_cube):
    
    
    print('wireCube')
    glBegin(GL_LINES)
    
    for edge in cubeEdges:
        for vertex in edge:
            glVertex3fv(cubeVertices[vertex])
    glEnd()

def solidCube():
    glBegin(GL_QUADS)
    for cubeQuad in cubeQuads:
        for cubeVertex in cubeQuad:
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()
