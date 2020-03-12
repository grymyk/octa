from octahedron import (
    vertices, faces, edges, getColorFace, printFaceNormal
)
from coords import archimedean_spiral, translate
from matrix import *
from transformations import translation_matrix

from OpenGL.GL import (
    glColor3fv, glVertex3fv, glColor4fv,
    glBegin, glEnd,
    GL_QUADS, GL_LINES, GL_TRIANGLES,
    glRotatef, glTranslatef
)

def set_vertices(number):
    new_vertices = []

    print( translate(vertices) )

    coords = translate(vertices)

    new_vertices.append(coords)
    
    # ~ coords = archimedean_spiral(number)

    # ~ for vertex in vertices:
        # ~ new_vert = []

        # ~ new_x = vertex[0] + coords[0]
        # ~ new_y = vertex[1] + coords[1]
        # ~ new_z = vertex[2] + coords[2]

        # ~ new_vert.append(new_x)
        # ~ new_vert.append(new_y)
        # ~ new_vert.append(new_z)

        # ~ new_vertices.append(new_vert)

    return new_vertices

class Shape():
    def __init__(self):
        self.active_face = 4
        self.face_colors = getColorFace(self.active_face)

        printFaceNormal(self.active_face)

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

        self.face_colors = getColorFace(self.active_face)
        self.add()

    def prevFace(self):
        print('prevFace')
        self.remove()
        self.active_face -= 1

        self.face_colors = getColorFace(self.active_face)

        self.add()

    def add(self):
        print('add')
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
