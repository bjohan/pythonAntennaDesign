from element import *

class DrivenMoxonElement(MoxonElement):
	def __init__(self, bendLength, straightLength, foldDirection, position, radius=0.025):
		MoxonElement.__init__(self,bendLength,straightLength, foldDirection, position, radius)

	def addNecGeometry(self, g):
		MoxonElement.addNecGeometry(self, g);
		drivenTag = g.tag-1;
		g.excite(drivenTag)
		return g


def makeDriven(e):
	return DrivenMoxonElement(e.bendLength, e.straightLength, e.foldDirection,
				e.position)

def makePassive(e):
	return MoxonElement(e.bendLength, e.straightLength, e.foldDirection,
				e.position)
		
