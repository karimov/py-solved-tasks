from unarygate import UnaryGate

class NotGate(UnaryGate):
    def __init__(self, label):
        UnaryGate.__init__(self, label)

    def performGateLogic(self):
        pin = self.getPin()

        if pin == 1:
            return 0
        else:
            return 1
