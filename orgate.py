from binarygate import BinaryGate

class OrGate(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a ==1 or b == 1:
            return 1
        else:
            return 0
