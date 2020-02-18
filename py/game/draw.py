import pygame


def draw_frame(player):
    print('draw_frame')
    
    bg_color_rgb = (0, 0, 0)
    
    screen.fill(bg_color_rgb)
    screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
