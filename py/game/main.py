import pygame
from player import Player

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()

player = Player()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

while running:  
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
            
    
    pressed_keys = pygame.key.get_pressed()
    
    player.update(pressed_keys)
    
    screen.fill((0, 0, 0))
    screen.blit(player.surf, player.rect)

    pygame.display.flip()
