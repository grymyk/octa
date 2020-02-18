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


########################################

light = (1, 2, 3)

faces = (
    [(1,0,0), (0,1,0), (0,0,1)],
    [(1,0,0), (0,0,-1), (0,1,0)],
    [(1,0,0), (0,0,1), (0,-1,0)],
    [(1,0,0), (0,-1,0), (0,0,-1)],
    [(-1,0,0), (0,0,1), (0,1,0)],
    [(-1,0,0), (0,1,0), (0,0,-1)],
    [(-1,0,0), (0,-1,0), (0,0,1)],
    [(-1,0,0), (0,0,-1), (0,-1,0)],
)

pygame.init()

display = (400, 400)
window = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

gluPerspective(45, 1, 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)
glEnable(GL_CULL_FACE)
glEnable(GL_DEPTH_TEST)
glCullFace(GL_BACK)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    clock.tick()
    
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    
    for face in faces:
        color = shade(face, blues, light)
        print(color)

        for vertex in face:
            glColor3fv( (color[0], color[1], color[2]) )
            glVertex3fv(vertex)
    glEnd()
    
    pygame.display.flip()
    
    # rotation start
    degrees_per_second = 360./5.
    degrees_per_millisecond = degrees_per_second / 1000.

    milliseconds = clock.tick()

    rotateAxis = (1, 1, 1);
    rotateAngle = milliseconds * degrees_per_millisecond;
    glRotatef(rotateAngle, rotateAxis[0], rotateAxis[1], rotateAxis[2])
    # rotation end