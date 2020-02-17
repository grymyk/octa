vertices = (
    (0, 0, -1), # bottom point -Z
    (1, 0, 0), (0, 1, 0), (0, -1, 0), (-1, 0, 0), # plane XOY
    (0, 0, 1) # top point +Z
)

edges = (
    (0, 1), (0, 2), (0, 4), (0, 3), # top segments -Z
    (1, 2), (2, 4), (4, 3), (3, 1), # middle segments plane XOY
    (1, 5), (2, 5), (4, 5), (3, 5) # botton segments +Z
)

faces = (
    (1, 2, 5), (1, 3, 5), (3, 4, 5), (2, 4, 5), # top faces ccw
    # ~ (1, 5, 2), (1, 5, 3), (3, 5, 4), (2, 5, 4), # top faces cw
    # ~ (0, 2, 4), (0, 3, 4), (0, 1, 3), (0, 1, 2),  # bottom faces cw
    (0, 4, 2), (0, 4, 3), (0, 3, 1), (0, 2, 1),  # bottom faces ccw
)

# color(red, green, blue)
face_colors = (
    [0, 0.2, 0], [0, 0.2, 0], [0, 0.2, 0], [0, 0.2, 0],
    [0.41, 0.95, 0.48], [0, 0.2, 0], [0, 0.2, 0], [0, 0.2, 0]
)

def getColorFace(n):
    len_face = len(faces)
    default_color = [0, 0.2, 0, 0.1]
    active_color = [0.41, 0.95, 0.48, 0.1]

    i = n

    if (n >= i):
        i = n % len_face

    # ~ print('face i:', i)

    face_colors = [default_color for color in range(len_face)]
    face_colors[i] = active_color

    return face_colors
