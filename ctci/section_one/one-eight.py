#!/usr/bin/python

'''1.8 Zero Matrix: Write an algorithm such that if an element in
                    an MxN matrix is 0, its entire row and column
                    are set to 0.

'''

import random
import numpy as np

def zeroMatrix(M,N):

    mat = [[random.randint(0,9) for n in range(N)] for m in range(M)]

    rows = set()
    columns = set()

    rc = set()

    print('Initial Matrix State:')
    printMatrix(mat)
    
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 0:
                #rc.add(i,j)
                rows.add(i)
                columns.add(j)

    for i in range(M):
        for j in range(N):
            if i in rows:
                mat[i][j] = 0
            if j in columns:
                mat[i][j] = 0

    print('Zeroed Matrix State:')
    printMatrix(mat)
                
def printMatrix(mat):
    for i in mat:
        print(i)
                
if __name__ == '__main__':
    zeroMatrix(5,6)
