# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 23:41:45 2020

@author: alexb
"""

class Vec:
    def __init__(self, contents = []):
        """constructor defaults to empty vector
           accepts list of elements to initialize a vector object with the 
           given list
        """
        self.elements = contents
        return
    
    def __abs__(self):
        """Overloads the built-in function abs(v)
            returns the Euclidean norm of vector v
        """
        output=0
        for i in self.elements:
            output+=i**2
        output=output**0.5
        return output
        pass
        
    def __add__(self, other):
        """Overloads the + operation to support Vec + Vec
         raises ValueError if vectors are not same length
        """        
        addedVect= Vec([])
        if len(self.elements)!=len(other.elements):
            raise ValueError("Vectors are not same length")
        else:
            for i in range(len(self.elements)):
                addedVect.elements.append(self.elements[i]+other.elements[i])
        return addedVect
    
    
    
    def __mul__(self, other):
        """Overloads the * operator to support 
            - Vec * Vec (dot product) raises ValueError if vectors are not same length in the case of dot product
            - Vec * float (component-wise product)
            - Vec * int (component-wise product)
            
        """
        if type(other) == Vec: #define dot product
            if len(self.elements)!=len(other.elements):
                raise ValueError("Vectors are not same length")
            else:
                output=0
                for i in range(len(self.elements)):
                    output=output+(self.elements[i]*other.elements[i])
            return output
        elif type(other) == float or type(other) == int: #scalar-vector multiplication
            #FIXME: IMPLEMENT
            output=Vec([])
            for i in self.elements:
                output.elements.append(i*other)
            return output
            
    
    def __rmul__(self, other):
        """Overloads the * operation to support 
            - float * Vec
            - int * Vec
        """
        output=Vec([])
        for i in self.elements:
            output.elements.append(i*other)
        return output
    
    def __str__(self):
        """returns string representation of this Vec object"""
        return str(self.elements) # does NOT need further implementation
    
    def __sub__(self, other):
        subbedVect= Vec([])
        if len(self.elements)!=len(other.elements):
            raise ValueError("Vectors are not same length")
        else:
            for i in range(len(self.elements)):
                subbedVect.elements.append(self.elements[i]-other.elements[i])
        return subbedVect