from octahedron import vertices, faces, edges, getColorFace
from coords import archimedean_spiral
from matrix import *
from transformations import translation_matrix

from OpenGL.GL import (
    glColor3fv, glVertex3fv, glColor4fv,
    glBegin, glEnd,
    GL_QUADS, GL_LINES, GL_TRIANGLES,
    glRotatef, glTranslatef
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

    TL = (
        (1, 0, x_delta),
        (0, 1, y_delta),
        (0, 0, 1)
    )

    tl_vertices = []

    for vertex in vertices:
        tl_vertex = multiply_matrix_vector(TL, vertex)
        tl_vertices.append(tl_vertex)

    for vertex in vertices:
        new_vert = []

        new_x = vertex[0] + x_value_change
        new_y = vertex[1] + y_value_change
        new_z = vertex[2] + z_value_change

        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)

    return new_vertices
    # ~ return tl_vertices

class Shape():
    def __init__(self):
        self.active_face = 0
        self.face_colors = getColorFace(self.active_face)

        self.count = 0
        self.shape_list = []
        
        self.add()
        
    def rotate(self, angle, axis):
        glRotatef(angle, axis[0], axis[1], axis[2])
        
    def translate(self, vector):
        glTranslatef(vector[0], vector[1], vector[2])

    def nextFace(self):
        print('nextFace')
        self.remove()
        self.active_face += 1
        # ~ print('active_face:', self.active_face)

        self.face_colors = getColorFace(self.active_face)
        self.add()

    def prevFace(self):
        print('prevFace')
        self.remove()
        self.active_face -= 1
        # ~ print('active_face:', self.active_face)

        self.face_colors = getColorFace(self.active_face)

        self.add()

    def add(self):
        self.count += 1
        self.shape_list.append( set_vertices(self.count) )

    def remove(self):
        len_shape_list = len(self.shape_list)

        if (len_shape_list):
            self.count -= 1
            self.shape_list.pop()

    def draw(self):
        len_shape_dict = len(self.shape_list)

        for index in range(len_shape_dict):
            self.shade(self.shape_list[index])

    def shadeTriangles(self, vertices):
        glBegin(GL_TRIANGLES)

        count_face = 0

        for face in faces:
            for vertex in face:
                glColor4fv(self.face_colors[count_face])
                glVertex3fv(vertices[vertex])

            count_face += 1
        glEnd()

    def shadeLines(self, vertices):
        gray = (0.5, 0.5, 0.5)

        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glColor3fv(gray)
                glVertex3fv(vertices[vertex])

        glEnd()

    def shade(self, vertices):
        self.shadeTriangles(vertices)
        self.shadeLines(vertices)

    def getCount(self):
        return self.count
