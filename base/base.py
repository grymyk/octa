import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from cube import *
from coords import *
   
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

def removeShapes(number):
    global shape_list
    
    len_shape_list = len(shape_list)
    
    if (len_shape_list):
        shape_list.pop()
    
def addShape(number):
    global shape_list

    shape_list.append(set_vertices(number))

def rightKeyHandle():
    print('RIGHT')

    global count
    
    count += 1
    print('count: ', count)
    
    addShape(count)

def leftKeyHandle():
    print('LEFT')

    global count
    
    count -= 1
    print('count: ', count)
    
    removeShapes(count)

def drawShape():
    len_shape_dict = len(shape_list)
    
    for index in range(len_shape_dict):
        Shape(shape_list[index])


def Shape(vertices):    
    glBegin(GL_LINES)
    
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    
    glEnd()

count = 0 
shape_list = []

def init():
    print('init')
    
    global count
    
    count += 1
    
    addShape(count)

def camera():
    pygame.init()
    display = (280, 260)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -50)


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rightKeyHandle()
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                leftKeyHandle()

def main():
    camera()
    
    init()
    
    while True:
        events()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
                
        drawShape()
        
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
