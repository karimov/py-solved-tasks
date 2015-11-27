class Connector:
    def __init__(self, fpin, tpin):
        self.from_pin = fpin
        self.to_pin = tpin

    def getFrom(self):
        return self.from_pin

    def getTo(self):
        return self.to_pin
