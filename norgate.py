from orgate import OrGate

class NorGate(OrGate):

    def performGateLogic(self):
        if OrGate.performGateLogic(self) == 1:
            return 0
        else:
            return 1
