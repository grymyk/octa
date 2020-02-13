from octahedron import vertices, faces, edges, face_colors
from coords import archimedean_spiral
from matrix import *
from transformations import translation_matrix

from OpenGL.GL import (
    glColor3fv, glVertex3fv,
    glBegin, glEnd,
    GL_QUADS, GL_LINES, GL_TRIANGLES,
)

def set_vertices(number):
    coords = archimedean_spiral(number)
    
    x_value_change = coords[0]
    y_value_change = coords[1]
    z_value_change = coords[2]

    new_vertices = []

    x_delta = 3
    y_delta = 0
    z_delta = 1

    tX = translation_matrix([3, 0, 0])
    print(tX)

    TL = (
        (1, 0, x_delta),
        (0, 1, y_delta),
        (0, 0, 1)
    )

    # ~ print('TL')
    # ~ print(TL)

    print(vertices)

    tl_vertices = []

    for vertex in vertices:
        tl_vertex = multiply_matrix_vector(TL, vertex)
        tl_vertices.append(tl_vertex)

    print('tl_vertices')
    print(tl_vertices)

    for vertex in vertices:
        new_vert = []

        new_x = vertex[0] + x_value_change
        new_y = vertex[1] + y_value_change
        new_z = vertex[2] + z_value_change

        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)
    
    print('new_vertices')
    print(new_vertices)

    return new_vertices
    # ~ return tl_vertices

class Shape():
    def __init__(self):
        self.count = 0 
        self.shape_list = []
        
        self.add()

    def remove(self):
        len_shape_list = len(self.shape_list)

        if (len_shape_list):
            self.count -= 1
            self.shape_list.pop()

    def add(self):
        self.count += 1
        self.shape_list.append( set_vertices(self.count) )

    def draw(self):
        len_shape_dict = len(self.shape_list)

        for index in range(len_shape_dict):
            self.render(self.shape_list[index])

    def render(self, vertices):
        glBegin(GL_TRIANGLES)

        count_face = 0

        for face in faces:
            x = 0

            for vertex in face:
                glColor3fv(face_colors[count_face])
                glVertex3fv(vertices[vertex])

            count_face += 1
        glEnd()

        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])

        glEnd()

    def getCount(self):
        return self.count
