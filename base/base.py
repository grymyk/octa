import pygame
import numpy

from pygame.locals import (
    QUIT, KEYDOWN, K_LEFT, K_RIGHT, DOUBLEBUF, OPENGL
)

from OpenGL.GL import (
    glClear, glEnable, 
    GL_CULL_FACE, GL_DEPTH_TEST, GL_BACK, GL_COLOR_BUFFER_BIT,
    GL_DEPTH_BUFFER_BIT, glCullFace,
    glTranslatef, glRotatef
)

from OpenGL.GLU import gluPerspective

from shape import Shape

def camera():
    pygame.init()

    display = (1280, 1260)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    dZ = -50
    glTranslatef(0.0, 0.0, dZ)


def events(shape):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                shape.add()
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                shape.remove()

def main():
    camera()
    
    shape = Shape()
    
    while True:
        events(shape)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        shape.draw()
        
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
