#! /usr/bin/python

# build 2 dimensional list or matrix
mymatrix = [[1,2,3],[4,5,6]]
print(mymatrix)

# get the rowcount
rowcount = len(mymatrix)
print(rowcount)

# get the column count
colcount = len(mymatrix[0])
print(colcount)

# get value of specific cell, row/col
cellval = mymatrix[1][1]
print(cellval)

# a square is a 2x2 matrix
# a cube is a 3x3 or 4x4 etc matrix