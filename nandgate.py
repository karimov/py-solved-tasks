from andgate import AndGate

class NandGate(AndGate):
    def performGateLogic(self):
        if AndGate.performGateLogic(self) == 1:
            return 0
        else:
            return 1
