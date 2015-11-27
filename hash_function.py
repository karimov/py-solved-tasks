


'''
Hasg function:
remainder-method
'''

def hash(aString, hashSize):
    sum = 0
    for i in range(len(aString)):
        sum = sum + ord(aString[i])*(i+1)
