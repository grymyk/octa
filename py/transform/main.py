import pygame as pg
from pygame.locals import *

from OpenGL.GLU import *

from cube import *
from keys import subscribe

def events(dict_cube):
    subscribe(dict_cube)

def form():
    pass
    
def draw(dict_cube):
    #solidCube()
    #wireCube(dict_cube)
    drawCubes(dict_cube)
        

def loop(dict_cube):
    events(dict_cube)
    
    form()
    
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    draw(dict_cube)
    
    pg.display.flip()

    pg.time.wait(10)

def camera():
    pg.init()
    
    display = (300, 400)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -15)

def main():
    dict_cube = {}
    
    camera()

    while True:
        loop(dict_cube)

if __name__ == "__main__":
    main()
