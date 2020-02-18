import pygame
import math

from pygame.locals import (
    QUIT, KEYDOWN, K_LEFT, K_RIGHT, DOUBLEBUF, OPENGL
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

lastPosX = 0
lastPosY = 0
zoomScale = 1.0
dataL = 0
xRot = 0
yRot = 0
zRot = 0

def mouseMove(event):
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

def camera():
    pygame.init()

    display = (680, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(90, (display[0]/display[1]), 0.1, 50.0)

    dX = 0
    dY = 0
    dZ = -5
    glTranslatef(dX, dY, dZ)


def events(shape):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # ~ shape.add()
                shape.nextFace()
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # ~ shape.remove()
                shape.prevFace()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                angle = 45
                axis = (0, 1, 0)
                
                shape.rotate(angle, axis)
       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                angle = -45
                axis = (0, 1, 0)
                
                shape.rotate(angle, axis)
                
        mouseMove(event)

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
