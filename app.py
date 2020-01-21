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
from octa import *

######### add to vectors.py
def normal(face):
    return(cross(subtract(face[1], face[0]), subtract(face[2], face[0])))

blues = matplotlib.cm.get_cmap('Blues')

def shade(face, color_map=blues, light=(1, 2 ,3)):
    return color_map(1 - dot(unit(normal(face)), unit(light)))

########################################

def axis_rotate(msec):
    degrees_per_sec = 360./5.
    degrees_per_msec = degrees_per_sec / 1000.

    rotateAngle = msec * degrees_per_msec;
    rotateAxis = (1, 1, 1);
    
    glRotatef(rotateAngle, rotateAxis[0], rotateAxis[1], rotateAxis[2])
     
class App:
    def __init__(self):
        print('__init__');
        
        self._running = True
        self.clock = None
        self.msec = None
        
        self.light = (1, 2, 3)

        self.octa = Octahedron()
 
    def on_init(self):
        print('on_init');
        
        pygame.init()
        self._running = True
        
        display = (400, 400)
        window = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

        gluPerspective(45, 1, 0.1, 50.0)
        
        glTranslatef(0.0, 0.0, -25)
        
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)
        glCullFace(GL_BACK)

        self.clock = pygame.time.Clock()
 
    def on_event(self, event):
        print('on_event');
        
        if event.type == pygame.QUIT:
            self._running = False
            
            
    def on_loop(self):
        print('on_loop')
        
        self.msec = self.clock.tick()
        faces = self.octa.getFaces()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glBegin(GL_TRIANGLES)
        
        for face in faces:
            color = shade(face, blues, self.light)

            for vertex in face:
                glColor3fv((color[0], color[1], color[2]))
                glColor3fv((color[0], color[1], color[2]))
                glVertex3fv(vertex)
        
        glEnd()

        pygame.display.flip()
        
        # ~ axis_rotate(self.msec)
    
    def on_render(self):
        print('on_render');
        
    def on_cleanup(self):
        print('on_event');
        
        pygame.quit()
     
    def on_execute(self):
        print('on_execute');
        
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
                
            self.on_loop()
            
            self.on_render()
            
            print('--')
            
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
