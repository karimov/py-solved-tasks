class Fraction:
    def __init__(self, top, bottom):
        if type(top) is int and type(bottom) is int:
            gcd = self.gcd(top, bottom)
            self.num = top//gcd
            self.dem = bottom//gcd
        else:
            raise ValueError("Only Integers")

    def __str__(self):
        return str(self.num)+"/"+str(self.dem)

    def __repr__(self):
        return repr(self.num)+"/"+repr(self.dem)

    def getNum(self):
        return self.num

    def getDem(self):
        return self.dem

    def __add__(self, other):
        pN = self.num*other.dem + self.dem*other.num
        pM = self.dem*other.dem
      #  common = self.gcd(pM, pN)
        return Fraction(pN, pM)

    def __radd__(self, other):
        pN = other.num*self.dem + other.dem*self.num
        pM = other.dem*self.dem
        return Fraction(pN, pM)

    def gcd(self, m, n):
        while m%n != 0:
            oldm = m
            oldn = n
            m = oldn
            n = oldm%oldn
        return n

    def __eq__(self, other):
        nN = self.num * other.dem
        nM = self.dem * other.num
        return nN == nM

    def __gt__(self, other):
        #pM = self.dem*other*dem
        pN1 = self.num*other.dem
        pN2 = other.num*self.dem
        return pN1 > pN2

    def __sub__(self, other):
        pN = self.num*other.dem - self.dem*other.num
        pM = self.dem * other.dem
       # gcd = self.gcd(pM,pN)
        return Fraction(pN, pM)

    def __mul__(self, other):
        pN = self.num*other.num
        pM = self.dem*other.dem
      #  gcd = self.gcd(pM, pN)
        return Fraction(pN, pM)

    def __div__(self, other):
        pN = self.num*other.dem
        pM = self.dem*other.num
       # gcd = self.gcd(pM, pN)
        return Fraction(pN, pM)

    def __lt__(self, other):
        if self.__gt__(other):
            return False
        return True

    def __ne__(self, other):
        if self.__eq__(other):
            return False
        return True
