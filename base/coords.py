import random
import math

def archimedean_spiral(t):
    coord = []
    
    angle = math.pi / 4 * t
    
    v = -2.4
    c = 0.5
    
    x = (v * t + c) * math.cos(angle)
    y = (v * t + c) * math.sin(angle)
    z = 0
    
    coord.append(x)
    coord.append(y)
    coord.append(z)
    
    return coord

def coors_random():
    max_distance = 100
    coord = []
    
    coord.append(random.randrange(-10, 10))
    coord.append(random.randrange(-10, 10))
    coord.append(random.randrange(-1*max_distance,-20) )

    return coord

