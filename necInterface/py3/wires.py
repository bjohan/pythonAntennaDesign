import numpy as np
np.set_printoptions(precision=3)
class Wire:
    def __init__(self, start, end, radius, name):
        self.start = np.array(start)
        self.end = np.array(end)
        self.radius = radius
        self.name = name
        self.segments = 35

    def addToNec(self, n):
        s = self.start
        e = Self.end
        n.wire(s[0], s[1], s[2], e[0], e[1], e[2], radius, self.segments)
        return n


    def length(self):
        return np.sqrt(sum((self.end-self.start)**2))

    def __str__(self):
        return "Wire named: "+str(self.name)+" from: "+str(self.start)+" to: "+str(self.end)+" length: "+str(self.length())+" radius: "+str(self.radius)


class ExcitedWire(Wire):
    def __init__(self, start, end, radius, name, excitePos):
        Wire.__init__(self, start, end, radius, name)
        if excitePos < 0 or excitePos > 1:
            raise ValueError("excitepos must be [0..1]")
        self.excitePos = excitePos

    def addToNec(self, n):
        n = Wire.addToNec(self, n)
        n.excite(n.tag-1, round(self.segments*self.excitePos))
        return n

    def __str__(self):
        return "Excited"+Wire.__str__(self)+" excited at: "+str(self.excitePos)

class LoadedWire(Wire):
    def __init__(self, start, end, radius, name, loadPos, load):
        Wire.__init__(self, end, radius, name)
        if loadPos < 0 or loadPos > 1:
            raise ValueError("excitepos must be [0..1]")
        self.loadPos = loadPos
        self.load = load

    def addToNec(self, n):
        n = Wire.addToNec(self, n)
        print("WARNING! load not implemented", self.name, "is just an ordinary wire")
        return n


    def __str__(self):
        return "Loaded"+Wire.__str__(self)+" loaded at: "+str(self.excitePos)+" with load: "+str(self.load)

