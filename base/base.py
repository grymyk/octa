import pygame

from pygame.locals import (
    DOUBLEBUF, OPENGL
)

from OpenGL.GL import (
    glClear,
    glEnable, glCullFace, GL_FRONT,
    GL_DEPTH_TEST,
    GL_CULL_FACE, GL_DEPTH_TEST, GL_BACK, GL_COLOR_BUFFER_BIT,
    GL_DEPTH_BUFFER_BIT, glCullFace,
    glTranslatef, glRotatef,
    GLfloat, glGetFloatv, GL_MODELVIEW_MATRIX, glScaled
)

from OpenGL.GLU import gluPerspective

from shape import Shape
from events import events

def camera():
    pygame.init()

    display = (680, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(90, (display[0]/display[1]), 0.1, 50.0)

    dX = 0
    dY = 0
    dZ = -5
    glTranslatef(dX, dY, dZ)


def main():
    camera()
    
    shape = Shape()
    
    while True:
        events(shape)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)
        
        shape.draw()

        pygame.display.flip()
        pygame.time.wait(10)


main()
