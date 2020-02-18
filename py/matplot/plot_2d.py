from vectors import *
from draw2d import *
from draw3d import *

top = (0,0,1)
bottom = (0,0,-1)
xy_plane = [(1,0,0),(0,1,0),(-1,0,0),(0,-1,0)]

edges = [Segment3D(top,p) for p in xy_plane] +\
[Segment3D(bottom, p) for p in xy_plane] +\
[Segment3D(xy_plane[i],xy_plane[(i+1)%4]) for i in range(0,4)]

# ~ draw3d(*edges)

octa_faces = [
    [(1, 0, 0), (0, 1, 0), (0, 0, 1)],
    [(1, 0, 0), (0, 0, -1), (0, 1, 0)],
    [(1, 0, 0), (0, 0, 1), (0, -1, 0)],
    [(1, 0, 0), (0, -1, 0), (0, 0, -1)],
    [(-1 ,0 ,0), (0, 0, 1), (0, 1, 0)],
    [(-1, 0, 0), (0, 1, 0), (0, 0, -1)],
    [(-1, 0, 0), (0, -1, 0), (0, 0, 1)],
    [(-1, 0, 0), (0, 0, -1), (0, -1, 0)],
]

octa_faces_1 = [
    [(0, 0, -1), (0, 1, 0), (1, 0, 0)],
    [(0, 0, -1), (0, -1, 0), (1, 0, 0)],
    [(0, 0, -1), (-1, 0, 0), (0, -1, 0)],
    [(0, 0, -1), (-1, 0, 0), (0, 1, 0)],
    [(1, 0, 0), (0, 1, 0), (0, 0, 1)],
    [(1, 0, 0), (0, -1, 0), (0, 0, 1)],
    [(0, -1, 0), (-1, 0, 0), (0, 0, 1)],
    [(0, 1, 0), (-1, 0, 0), (0, 0, 1)]
]

octa_faces_2 = [
    [(0, 0, -1), (0, 1, 0), (1, 0, 0)],
    [(0, 0, -1), (0, -1, 0), (1, 0, 0)],
    [(0, -1, 0), (-1, 0, 0), (0, 0, 1)],
    [(0, 1, 0), (-1, 0, 0), (0, 0, 1)]
]


# normal and unit vectors
Points3D( (1, 1, 1) ),
Arrow3D( (0.5773502691896258, 0.5773502691896258, 0.5773502691896258) ),
Points3D( (1, 1, -1) ),
Arrow3D( (0.5773502691896258, 0.5773502691896258, -0.5773502691896258) ),
Points3D( (1, -1, 1) ),
Arrow3D( (0.5773502691896258, -0.5773502691896258, 0.5773502691896258) ),
Points3D( (1, -1, -1) ),
Arrow3D( (0.5773502691896258, -0.5773502691896258, -0.5773502691896258) ),
Points3D( (-1, 1, 1) ),
Arrow3D( (-0.5773502691896258, 0.5773502691896258, 0.5773502691896258) ),
Points3D( (-1, 1, -1) ),
Arrow3D( (-0.5773502691896258, 0.5773502691896258, -0.5773502691896258) ),
Points3D( (-1, -1, 1) ),
Arrow3D( (-0.5773502691896258, -0.5773502691896258, 0.5773502691896258) ),
Points3D( (-1, -1, -1) ),
Arrow3D( (-0.5773502691896258, -0.5773502691896258, -0.5773502691896258) )

blues = matplotlib.cm.get_cmap('Blues')

def render(faces, light=(1,2,3), color_map=blues, lines=None):
    polygons = []
    arrows = []
    points = []
    
    for face in faces:
        normal_vector = normal(face)
        print('Points3D(', normal_vector, '),')
        
        unit_normal = unit(normal_vector)
        print('Arrow3D(', unit_normal, '),')
    
        arrows.append( Arrow3D(normal_vector) )
        points.append( Points3D(normal_vector) )
        
    # ~ draw3d(
        
    # ~ )
    # ~ draw3d(*arrows, *edges)
    draw3d(*arrows, *points)
    
        # ~ if unit_normal[2] > 0:
            #c = color_map(1 - dot(unit(normal(face)), unit(light)))
            
            #p = Polygon2D(*face_to_2d(face), fill=c, color=lines)
            #polygons.append(p)
            
    # ~ draw2d(*polygons, axes=False, origin=False, grid=None)


# ~ render(octa_faces, lines=black)
render(octa_faces_2, lines=black)
