from logicgate import LogicGate

class BinaryGate(LogicGate):
    def __init__(self, label):
        LogicGate.__init__(self, label)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
             return int(input("Enter pinA input for gate"+self.getLabel()+"->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter pinB input for gate"+self.getLabel()+"->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("ERROR: NO EMPTY PINS")
