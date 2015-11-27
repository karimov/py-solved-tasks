from logicgate import LogicGate

class UnaryGate(LogicGate):
    def __init__(self, label):
        LogicGate.__init__(self, label)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate"+self.getLabel()+"->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("ERROR: NO EMPTY PINS")
