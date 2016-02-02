

'''
Hasg function:
remainder-method
'''

def hash(aString, hashSize):
    sum = 0
    for pos in range(len(aString)):
        sum = sum + ord(aString[pos])*(pos+1)

    return sum%hashSize
