import pygame, math

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

screen = 512
main_surface = pygame.display.set_mode( (screen, screen) )
my_clock = pygame.time.Clock()

def draw_tree(order, theta, size, position, heading, color=(0,0,0), depth=0):
    print('draw_tree')
    
    trunk_ratio = 0.29
    # How big is the trunk relative to whole tree?
    trunk = size * trunk_ratio # length of trunk
    delta_x = trunk * math.cos(heading)
    delta_y = trunk * math.sin(heading)
    (u, v) = position
    newposition = (u + delta_x, v + delta_y)
    
    print(position, newposition)
    
    pygame.draw.line(main_surface, color, position, newposition)

    if order > 0:
        # Draw another layer of subtrees
        # These next six lines are a simple hack to make the two major halves
        # of the recursion different colors. Fiddle here to change colors
        # at other depths, or when depth is even, or odd, etc.
        if depth == 0:
            color1 = (255, 0, 0)
            color2 = (0, 0, 255)
        else:
            color1 = color
            color2 = color
            
            # make the recursive calls to draw the two subtrees
            newsize = size*(1 - trunk_ratio)
            draw_tree(order-1, theta, newsize, newposition, heading-theta, color1, depth+1)
            draw_tree(order-1, theta, newsize, newposition, heading+theta, color2, depth+1)

running = True

order = 4
theta = 0
xPos = screen
yPos = screen
size = screen
angle = math.pi

draw_tree(order, theta, size, (xPos, yPos), angle)

while running:  
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
            
    # Updates - change the angle
    theta += 0.1
    
    # Draw everything
    main_surface.fill((255, 255, 0))
    
    xPos //= 2
    yPos -= 50
    angle /= 2
    size *= 0.9
    
    print(theta)
    
    # ~ draw_tree(order, theta, size, (xPos, yPos), angle)
    
    pygame.display.flip()

