from xorgate import XorGate
from andgate import AndGate

class HalfAdder2(XorGate, AndGate):
#    def __init__(self):
#        self.sum = None
#        self.carry = None

    def performGateLogic(self):
        sum = XorGate.performGateLogic(self)
        carry = AndGate.performGateLogic(self)
        return (sum, carry)

    def halfader(self, a, b):
        s = XorGate(a, b)
        c = AndGate(a, b)
        return (s,c)
