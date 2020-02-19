def subtract(v1, v2):
#     print('v1:', v1)
#     print('v2:', v2)

    return tuple( v1 - v2 for (v1, v2) in zip(v1, v2) )

def cross(u, v):
    ux, uy, uz = u
    vx, vy, vz = v
        
    return (uy*vz - uz*vy, uz*vx - ux*vz, ux*vy - uy*vx)

def getNormal(face_vertices):
    u = subtract(face_vertices[1], face_vertices[0])
    v = subtract(face_vertices[2], face_vertices[0])
    
#     print('u:', u)
#     print('v:', v)
    
    return ( cross(u, v) )
