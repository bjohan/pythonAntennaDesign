from element import *

class DrivenElement(Element):
	def __init__(self, length, position, radius=0.025):
		Element.__init__(self, length, position, radius)

	def addNecGeometry(self, g):
		Element.addNecGeometry(self, g);
		drivenTag = g.tag-1;
		g.excite(drivenTag)
		return g


def makeDriven(e):
	return DrivenElement(e.bendLength, e.straightLength, e.foldDirection,
				e.position)

def makePassive(e):
	return Element(e.bendLength, e.straightLength, e.foldDirection,
				e.position)
		
