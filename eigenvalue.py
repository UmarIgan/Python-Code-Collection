#determinant=https://stackoverflow.com/questions/10003232/python-determinant-calculationwithout-the-use-of-external-libraries
from itertools import product, islice
import numpy as np

def determinant(M):#calculating determinant, found on stackoverflow
    prod=1
    dim = len(M)
    if dim == 1:
        return prod * M.pop().pop()
    it = product(range(1,dim),repeat=2)
    prod *= M[0][0]
    return det([[M[x][y]-M[x][0]*(M[0][y]/M[0][0]) for x,y in islice(it,dim-1)] for i in range(dim-1)],prod)

def eigenvalue(arr):
    x=[]
    col=3
    det=determinant(arr)
    for i in mat:
        for j in i:
            x.append(j*(1/det))
    return ([x[i:i+col] for i in range(0, len(x), col)])
matrix=np.random.rand(4,4)#4x4 matrix
eigen_mat=eigenvalue(matrix)
eigen_mat
