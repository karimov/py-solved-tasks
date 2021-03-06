from binarygate import BinaryGate

class HalfAdder(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return (0,0)
        elif a == 0 and b == 0:
            return (0,0)
        else:
            return (1,0)
