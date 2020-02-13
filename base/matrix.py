def dot(u, v):
    return sum([coord1 * coord2 for coord1, coord2 in zip(u,v)])

def multiply_matrix_vector(matrix, vector):
    return tuple( dot(row, vector) for row in matrix )

def matrix_multiply(a,b):
    return tuple( tuple(dot(row, col) for col in zip(*b)) for row in a )
