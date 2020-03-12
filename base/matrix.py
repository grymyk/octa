def dot(u, v):
    return sum([coord1 * coord2 for coord1, coord2 in zip(u,v)])

def multiply_matrix_vector(matrix, vector):
    return tuple( dot(row, vector) for row in matrix )

def matrix_multiply(a,b):
    return tuple( tuple(dot(row, col) for col in zip(*b)) for row in a )
    
def gomoCoord(vectors):
    lsts = []
    w = 1
    
    for vector in vectors:
        lst = list(vector)
        lst.append(w)
        
        lsts.append(lst)
    
    return lsts
    
def euclidCoord(vectors):
    lsts = []
    
    for vector in vectors:
        lst = list(vector)
        lst.pop()
        
        lsts.append(lst)
    
    return lsts
    
def translation_matrix(vector):
    tl = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]

    tl[0][3] = vector[0]
    tl[1][3] = vector[1]
    tl[2][3] = vector[2]
    
    return tl 

