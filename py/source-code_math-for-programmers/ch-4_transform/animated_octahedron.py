import pygame
import os
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import matplotlib.cm
from vectors import *
from math import *

from camera import Camera
camera=Camera('animated-octahedron-frames',[100 * x for x in range(1,50)],comic_strip=7,dir=os.path.join('figs','animated-octahedron-frames'))

def normal(face):
    return(cross(subtract(face[1], face[0]), subtract(face[2], face[0])))

blues = matplotlib.cm.get_cmap('Blues')

def shade(face,color_map=blues,light=(1,2,3)):
    return color_map(1 - dot(unit(normal(face)), unit(light)))

light = (1,2,3)
faces = [
    [(1,0,0), (0,1,0), (0,0,1)],
    [(1,0,0), (0,0,-1), (0,1,0)],
    [(1,0,0), (0,0,1), (0,-1,0)],
    [(1,0,0), (0,-1,0), (0,0,-1)],
    [(-1,0,0), (0,0,1), (0,1,0)],
    [(-1,0,0), (0,1,0), (0,0,-1)],
    [(-1,0,0), (0,-1,0), (0,0,1)],
    [(-1,0,0), (0,0,-1), (0,-1,0)],
]

def Axes():
    axes =  [
        [(-1000,0,0),(1000,0,0)],
        [(0,-1000,0),(0,1000,0)],
        [(0,0,-1000),(0,0,1000)]
    ]

    glBegin(GL_LINES)
    for axis in axes:
        for vertex in axis:
            glColor3fv((1,1,1))
            glVertex3fv(vertex)
    glEnd()

pygame.init()
display = (400,400)
window = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

gluPerspective(45, 1, 0.1, 50.0)

glTranslatef(0.0,0.0, -5)

glEnable(GL_CULL_FACE)
glEnable(GL_DEPTH_TEST)
glCullFace(GL_BACK)

camera.set_window(window)

milliseconds = 0
while camera.is_shooting():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()



    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    degrees_per_second = 360./5.
    degrees_per_milisecond = degrees_per_second / 1000.
    glRotatef(milliseconds * degrees_per_milisecond, 1,1,1)
    # glRotatef(10, 1,1,1)

    glBegin(GL_TRIANGLES)
    for face in faces:
        color = shade(face,blues,light)
        for vertex in face:
            glColor3fv((color[0], color[1], color[2]))
            glVertex3fv(vertex)
    glEnd()
    milliseconds = camera.tick()
    pygame.display.flip()

    print(camera.get_fps())
