from octahedron import vertices, faces, edges, face_colors
from coords import archimedean_spiral

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

    for vert in vertices:
        new_vert = []

        new_x = vert[0] + x_value_change
        new_y = vert[1] + y_value_change
        new_z = vert[2] + z_value_change

        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)
    
    return new_vertices

class Shape():
    def __init__(self):
        self.count = 0 
        self.shape_list = []
        
        self.add()

    def getCount(self):
        return self.count
    
    def add(self):
        self.count += 1
        self.shape_list.append( set_vertices(self.count) )
        
    def remove(self):
        len_shape_list = len(self.shape_list)

        if (len_shape_list):
            self.count -= 1
            self.shape_list.pop()

    def render(self, vertices):
        glBegin(GL_TRIANGLES)
        for face in faces:
            x = 0

            for vertex in face:
                x += 1

                glColor3fv(face_colors[x])
                glVertex3fv(vertices[vertex])
        glEnd()

        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])

        glEnd()
        
    def draw(self):
        len_shape_dict = len(self.shape_list)
        
        for index in range(len_shape_dict):
            self.render(self.shape_list[index])
