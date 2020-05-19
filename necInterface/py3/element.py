import random


class Element:
    def __init__(self, length=None, position=None, radius = 0.025):
        self.maxGeom = 4.0
        self.length = length;
        self.position = position
        self.radius = radius

    def __str__(self):
        s = "Element information:"
        s += "\n\t Length: " + str(self.length)
        s += "\n\t Radius: " + str(self.radius)
        s += "\n\t Position on boom: " + str(self.position) + "\n"
        return s

    def addNecGeometry(self, g):
        ylength = 0.5 * self.length

        g.wire(self.position, -ylength, 0,
               self.position, ylength, 0, self.radius)
        return g
