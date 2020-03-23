# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 12:23:47 2020

@author: alexb
"""

def gcd(a,b):
    #FIXME: IMPLEMENT THIS METHOD
    if (b != 0):
        return gcd(b, a%b)
    else:
        return a
    
def modExp(b, n, m):
    if (m == 1):
        return 0
    c = 1
    expoCounter = 0
    for expoCounter in range(0, n):
        c = (c * b) % m
    return c

def digits2letters(digits):
    """converts a string of double digits without spaces in the range 00-25 to a string of letters A-Z"""
    letter2digit = {"A" : "00", "B" : "01", "C" : "02", "D" : "03", "E" : "04", 
                  "F" : "05", "G" : "06", "H" : "07", "I" : "08", "J" : "09",
                  "K" : "10", "L" : "11", "M" : "12", "N" : "13", "O" : "14",  
                  "P" : "15", "Q" : "16", "R" : "17", "S" : "18", "T" : "19",
                  "U" : "20", "V" : "21", "W" : "22", "X" : "23", "Y" : "24", 
                  "Z" : "25"}
        
    digit2letter = dict((v,k) for k,v in letter2digit.items())  #creating a dictionary with keys and values exchanged
        
    letters = ""
    start = 0  #initializing starting index of first digit
    for i in range(0, len(digits), 2):
        digit = digits[start : start + 2]  # accessing the double digit
        letters += digit2letter[digit]     # concatenating to the string of letters
        start += 2                         # updating the starting index for next digit
    
    return letters

def letters2digits(letters):
    """converts a string of letters A-Z to a string of double digits without spaces in the range 00-25"""
    letter2digit = {"A" : "00", "B" : "01", "C" : "02", "D" : "03", "E" : "04", 
                  "F" : "05", "G" : "06", "H" : "07", "I" : "08", "J" : "09",
                  "K" : "10", "L" : "11", "M" : "12", "N" : "13", "O" : "14",  
                  "P" : "15", "Q" : "16", "R" : "17", "S" : "18", "T" : "19",
                  "U" : "20", "V" : "21", "W" : "22", "X" : "23", "Y" : "24", 
                  "Z" : "25"}
        
    digits = ""  #initializing digits string
    letters = "".join(letters.split()) #removing whitespaces in the text

    
    for i in range(0, len(letters)):
        if(letters[i].isalpha()):
            letter = letters[i].upper()  #converting to uppercase
            digit = letter2digit[letter]
            digits += digit     # concatenating to the string of digits
    
    return digits

def blocksize(n):
    """returns the size of a block in an RSA encrypted string"""
    twofive = "25"
    while int(twofive) < n:
        twofive += "25"
    return len(twofive) - 2

#Problem #1
    
def modinv(a,m):
    """returns the inverse of a modulo m
    INPUT: a - integer
           m - positive integer
    OUTPUT: a inverse as an integer
    """
    if (gcd(a,m) != 1):
        raise ValueError("The given values are not relatively prime")
    else:
        x = 1
        while x in range (1,m):
            if ((a * x) % m) == 1:
                return x
            x+=1
    return 1

def affineEncrypt(text, a, b):
    """encrypts the plaintext 'text', using an affine transformation key (a, b)
    INPUT:  text - plaintext as a string of letters
            a - integer satisfying gcd(a, 26) = 1.  Raises error if such is not the case
            b - integer 
            
    OUTPUT: The encrypted message as a string of characters
    """
    if (gcd(a,b) != 1):
        raise ValueError("The given values are not relatively prime")
    if (a > b):
        raise ValueError("The given values are not relatively prime")
    else:
        coded = letters2digits(text)
        start = 0
        letters = ""
        for i in range(0, len(coded), 2):
            digit = coded[start : start + 2]              # accessing the double digit
            newNum = ((a * int(digit) + b) % 26)
            strNewNum = ""
            if (int(newNum) < 10):
                    strNewNum = "0" + str(newNum)
            else:
                strNewNum = str(newNum)
            letters += strNewNum                        # concatenating to the string of letters
            start += 2                                    # updating the starting index for next digit
    fullEncode = digits2letters(letters)
    return fullEncode

def affineDecrypt(ciphertext, a, b):
    """decrypts the string 'ciphertext', which was encrypted using an affine transformation key (a, b)
    INPUT:  ciphertext - a string of encrypted letters
            a - integer satisfying gcd(a, 26) = 1.  
            b - integer 
            
    OUTPUT: The decrypted message as a string of characters
    """
    if (gcd(a,b) != 1):
        raise ValueError("The given values are not relatively prime")
    else:
        coded = letters2digits(ciphertext)
        start = 0
        letters = ""
        for i in range(0, len(coded), 2):
            digit = coded[start : start + 2]
            decodeA = modinv(a, 26)
            newNum = ((decodeA * (int(digit) - b)) % 26)
            strNewNum = ""
            if (int(newNum) < 10):
                strNewNum = "0" + str(newNum)
            else:
                strNewNum = str(newNum)
            letters += strNewNum
            start += 2
    fullEncode = digits2letters(letters)
    return fullEncode

def encryptRSA(m, p, q, e):
    """encrypts the plaintext m, using RSA and the key (p * q, e)
    INPUT:  m - plaintext as a string of letters
            p, q - prime numbers used as part of the key n = p * q to encrypt the ciphertext
            e - integer satisfying gcd((p-1)*(q-1), e) = 1
            
    OUTPUT: The encrypted message as a string of digits
    """
    if (gcd((p - 1) * (q - 1), e ) != 1) :
        raise ValueError("The given values are not relatively prime")
    else :
        coded = letters2digits(m)
        start = 0
        letters = ""
        n = p * q
        l = blocksize(n)
        for i in range(0, len(coded), l):
            digit = coded[start : start + l]
            encryptingLetter = str(modExp(int(digit), e, n))
            if(len(encryptingLetter) < l):
                encryptingLetter = "0" + encryptingLetter
            letters += encryptingLetter
            start += l
    return letters

def decryptRSA(c, p, q, e):
    """decrypts the cipher c, which was encrypted using the key (p * q, e)
    INPUT:  c - ciphertext as a string of digits
            p, q - prime numbers used as part of the key n = p * q to encrypt the ciphertext
            e - integer satisfying gcd((p-1)*(q-1), e) = 1
            
    OUTPUT: The decrypted message as a string of letters
    """
    if (gcd((p - 1) * (q - 1), e ) != 1) :
        raise ValueError("The given values are not relatively prime")
    else :
        start = 0
        letters = ""
        n = p * q
        new_n = (p - 1) * (q - 1)
        inverse_n = modinv(e, new_n)
        l = blocksize(n)
        coded = "".join(c.split())
        for i in range(0, len(coded), l):
            digit = coded[start : start + l]
            encryptingLetter = str(modExp(int(digit), inverse_n, n))
            if(len(encryptingLetter) < l):
                encryptingLetter = "0" + encryptingLetter
            letters += str(encryptingLetter)
            start += l
    fullDecode = digits2letters(letters)
    return fullDecode
        
    