
class WaterJug:
    def __init__(self, jug1size, jug2size, goal):
        self.j1s = jug1size
        self.j2s = jug2size
        self.goal = goal
        self.a = 0
        self.b = 0

    def wCheck(self):
        ok = False
        while not ok:
            if self.a == self.goal or self.b == self.goal:
                ok = True
            if self.a == 0:
                self.fillA()
            elif self.a > 0 and self.b != self.j2s:
                self.pourAtoB()
            elif self.a > 0 and self.b == self.j2s:
                self.emptyB()

    def fillA(self):
        self.a = self.j1s
        print(self.a,self.b)

    def fillB(self):
        self.b = self.j2s
        print(self.a,self.b)

    def pourAtoB(self):
        ok = False
        while not ok:
            if self.b == self.j2s or self.a == 0:
                ok = True
            else:
                self.b += 1
                self.a -= 1
        print(self.a, self.b)

    def emptyB(self):
        self.b = 0
        print(self.a,self.b)

    def emptyA(self):
        self.a = 0
        print(self.a,self.b)

    def getA(self):
        return self.a

    def setA(self):
        self.a = self.j1s
        print(self.a)
