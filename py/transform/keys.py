import pygame
from pygame.locals import (
    QUIT, KEYDOWN,
    K_UP, K_DOWN, K_LEFT, K_RIGHT
)

from cube import getCubes, drawCubes,  wireCube

def upKeyHandle(dict_cube):
    print('upKeyHandle')
    number_cube = 1

    cubes = getCubes(number_cube)
    
    drawCubes(cubes)
    
    # ~ wireCube()
    

def subscribe(dict_cube):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('LEFT')


            if event.key == pygame.K_UP:
                print('UP')
                
                upKeyHandle(dict_cube)

                
            if event.key == pygame.K_RIGHT:
                print('RIGHT')
                
            
            if event.key == pygame.K_DOWN:
                print('DOWN')
