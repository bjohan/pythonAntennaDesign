class Geometry:
    def __init__(self, name):
        self.elements = []
        self.name = name


    def addElement(self, element):
        self.elements.append(element)

    def __str__(self):
        s = "Antenna named %s\n"%(self.name)
        for e in self.elements:
            s+='\t'+str(e)+'\n'
        return s
