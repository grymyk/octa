import pygame
from pygame.locals import *

import math

from OpenGL.GL import *
from OpenGL.GLU import *

lastPosX = 0
lastPosY = 0
zoomScale = 1.0
dataL = 0
xRot = 0
yRot = 0
zRot = 0

def Cube():
    verticies = (
        (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
        (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1)
    )

    edges = (
        (0, 1), (0, 3), (0, 4), (2, 1), (2, 3), (2, 7),
        (6, 3), (6, 4), (6, 7), (5, 1), (5, 4), (5, 7)
    )

    glBegin(GL_LINES)

    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

    # print(repr(verticies[0][0])+','+repr(verticies[0][1]));
 
    glBegin( GL_POINTS )
    glColor3f(1,1,1)

    for i in range(0,8):
         glVertex3f(verticies[i][0], verticies[i][1], verticies[i][2])
    glEnd()
 
def mouseMove(event):
    print(event)
    
    global lastPosX, lastPosY, zoomScale, xRot, yRot, zRot
 
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4: # wheel rolled up
        glScaled(1.05, 1.05, 1.05)
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5: # wheel rolled down
        glScaled(0.95, 0.95, 0.95)
    if event.type == pygame.MOUSEMOTION:
        x, y = event.pos
        dx = x - lastPosX
        dy = y - lastPosY

        mouseState = pygame.mouse.get_pressed()

        if mouseState[0]:
            modelView = (GLfloat * 16)()
            print(modelView)

            mvm = glGetFloatv(GL_MODELVIEW_MATRIX, modelView)
   
            # To combine x-axis and y-axis rotation
            temp = (GLfloat * 3)()
            temp[0] = modelView[0]*dy + modelView[1]*dx
            temp[1] = modelView[4]*dy + modelView[5]*dx
            temp[2] = modelView[8]*dy + modelView[9]*dx

            norm_xy = math.sqrt(temp[0]*temp[0] + temp[1]*temp[1] + temp[2]*temp[2])

            glRotatef(math.sqrt(dx*dx+dy*dy), temp[0]/norm_xy, temp[1]/norm_xy, temp[2]/norm_xy)

        lastPosX = x
        lastPosY = y

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        mouseMove(event)

def camera():
    pygame.init()

    display = (1000, 750)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL, RESIZABLE)

    gluPerspective(45, (1.0 * display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

def main():
    camera()

    while True:
        events()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        Cube()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
