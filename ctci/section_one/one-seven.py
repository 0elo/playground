#!/usr/bin/python

'''1.7 Rotate Matrix: Given an image represented by an NxN matrix,
                      where each pixel in the image is 4 bytes,
                      write a method to rotate the image by 90
                      degrees. Can you do this in place?

'''

import random
import numpy as np

def rotateMatrixNP(N):
    mat = np.random.randint(10, size=(N,N))

    print('\nInitial NP Matrix State:')
    print(mat)
    print('\nRotated NP Matrix State:')
    print(np.rot90(mat, -1))

def rotateMatrixClockwise(N):
    mat = [[random.randint(0,9) for i in range(N)] for j in range(N)]
    print('\nInitial Matrix State:')
    printMatrix(mat)  
    for layer in range(int(N/2)):
        first = layer
        last = N - 1 - first

        for i in range(first, last):
            offset = i - first

            top = mat[first][i]
            mat[first][i] = mat[last-offset][first]
            mat[last-offset][first] = mat[last][last-offset]
            mat[last][last-offset] = mat[i][last]
            mat[i][last] = top

    print('\nRotated Matrix State:')
    printMatrix(mat)

def rotateMatrixCounterwise(N):
    mat = [[random.randint(0,9) for i in range(N)] for j in range(N)]
    print('\nInitial Matrix State:')
    printMatrix(mat)
    for layer in range(int(N/2)):
        first = layer
        last = N - 1 - first
        for i in range(first,last):
            offset = i -first
            top = mat[first][i]
            mat[first][i] = mat[i][last]
            mat[i][last] = mat[last][last-offset]
            mat[last][last-offset] = mat[last-offset][first]
            mat[last-offset][first] = top

    print('\nRotated Matrix State:')
    printMatrix(mat)
    
def printMatrix(mat):
    for i in mat:
        print(i)
    
if __name__ == '__main__':
    rotateMatrixNP(4)
    rotateMatrixClockwise(4)
    rotateMatrixCounterwise(4)
