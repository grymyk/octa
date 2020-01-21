import pygame
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT,
    K_ESCAPE, KEYDOWN, QUIT, DOUBLEBUF, OPENGL
)

from OpenGL.GL import (glClear, glTranslatef, glEnable, glBegin,
    GL_CULL_FACE, GL_DEPTH_TEST, GL_BACK, GL_COLOR_BUFFER_BIT,
    GL_DEPTH_BUFFER_BIT, glBegin, GL_TRIANGLES, glColor3fv, glVertex3fv,
    glCullFace, glEnd, glRotatef
)
 
from OpenGL.GLU import gluPerspective

import matplotlib.cm

from vectors import cross, subtract, dot, unit

######### add to vectors.py
def normal(face):
    return(cross(subtract(face[1], face[0]), subtract(face[2], face[0])))

blues = matplotlib.cm.get_cmap('Blues')

def shade(face, color_map=blues, light=(1, 2 ,3)):
    return color_map(1 - dot(unit(normal(face)), unit(light)))
 
class App:
    def __init__(self):
        print('__init__')
    
    def on_execute(self):
        print('on_execute')
        
        
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
