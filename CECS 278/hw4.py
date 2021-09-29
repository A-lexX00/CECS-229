# -*- coding: utf-8 -*-
"""
Created on Sat May  9 18:47:52 2020

@author: alexb
"""

class Matrix:
    
    def __init__(self, givenRows):
        self.row = len(givenRows)
        self.col = len(givenRows[0])
        self.givenRows = givenRows
        
    def getRow (self, h):
        row = []
        for j in range(self.col):
                row.append(self.givenRows[h - 1][j])
        return row
    
    def getCol (self, w):
        col = []
        for j in range(self.row):
                col.append(self.givenRows[j][w - 1])
        return col
    
    def getRowSpace (self):
        return self.row
    
    def getColSpace (self):
        return self.col
    
    def getEntry (self, i, j):
        return self.givenRows[i][j]
    
    def setEntry (self, i , j, a):
        self.givenRows[i - 1][j - 1] = a
        
    def setRow(self, i, a):
        if(i < self.row and len(a) == self.row):
            self.row = a
            for j in range(self.col):
                self.givenRows[j][i] = a[j]
        else:
            print("Row length not matching")
    
    def setCol(self, j, b):
        if(j < self.col and len(b) == self.col):
            self.col = b
            for i in range(self.row):
                self.givenRows[i][j] = b[i]
        else:
            print("Column length not matching")
            
    def getdiag(self, k):
        diagonalList = []
        if(k > 0):
            for i in range(self.row):
                if(k + i < self.col):
                    diagonalList.append(self.givenRows[i][k + i])
        else:
            for i in range(self.row):
                if(abs(k) + i < self.col):
                    diagonalList.append(self.givenRows[abs(k) + i][i])
        return diagonalList
        
    def __add__(self, other):
        matrixAddition = []
        if (self.row != other.row or self.col != other.col):
            ValueError("Trying to add matrixes of varying sizes!")
        else:
            for i in range(self.row):
                newRow = []
                for j in range(self.col):
                    addition = self.givenRows[i][j] + other.givenRows[i][j]
                    newRow.append(addition)
                matrixAddition.append(newRow)
        return Matrix(matrixAddition)
    
    def __sub__(self, other):
        matrixSubtraction = []
        if (self.row != other.row or self.col != other.col):
            ValueError("Trying to subtract matrixes of varying sizes!")
        else:
            for i in range(self.row):
                newRow = []
                for j in range(self.col):
                    subs = self.givenRows[i][j] - other.givenRows[i][j]
                    newRow.append(subs)
                matrixSubtraction.append(newRow)
        return Matrix(matrixSubtraction)
        
    def __mul__(self, other):  
        if type(other) == float:
            print("FIXME: Insert implementation of MATRIX-SCALAR multiplication")  #REPLACE
        elif type(other) == Matrix:
            print("FIXME: Insert implementation of MATRIX-MATRIX multiplication") #REPLACE
        elif type(other) == Vec:
            print("FIXME: Insert implementation for MATRIX-VECTOR multiplication")  #REPLACE
        else:
            print("ERROR: Unsupported Type.")
        return
    
    def __rmul__(self, other):  
        if type(other) == float:
            print("FIXME: Insert implementation of SCALAR-MATRIX multiplication")  #REPLACE
        else:
            print("ERROR: Unsupported Type.")
        return
    
    def __str__(self):
        """prints the column """
        output = ""
        for i in range(self.row):
            for j in range(self.col):
                output = output + str(self.givenRows[i][j]) + "\t"
            output = output + "\n"
        return output