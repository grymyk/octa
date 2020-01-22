from vectors import cross, subtract, dot, unit, normal
import matplotlib.cm

blues = matplotlib.cm.get_cmap('Blues')

def shade(face, color_map=blues, light=(1, 2 ,3)):
    return color_map(1 - dot(unit(normal(face)), unit(light)))
