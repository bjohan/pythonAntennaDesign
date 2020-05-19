from band import *
from element import *
from drivenElement import *
from antenna import *
from compute import *
from analyzer import *
from plothelper import *
from population import *
from individual import *

band2Meter = Band(144.0,146.0, '2 meter')

bands = [band2Meter]

lengths = [ 997,
    997*0.96, 
    941,
    932,
    924,
    916,
    909,
    903,
    898,
    893,
    888,
    884];

positions = [0,
    497,
    652, 
    1024, 
    1469, 
    1986, 
    2566, 
    3186, 
    3838, 
    4521, 
    5234, 
    5979]; 

print("Adding elements to antenna")
ant = Antenna()
#ant.addElement(DrivenElement(0, 0.98*0.5, 'north', 0.497))
n = 0
for l,p in zip(lengths, positions):
    print("Element", n, end=' ')
    if n == 1:
        print("Driven")
        ant.addElement(DrivenElement( l/1000.0 , p/1000.0, 0.005))
    else:
        print("Passive")
        ant.addElement(Element(l/1000.0 ,  p/1000.0, 0.005))
    n+=1
#ant.addElement(element1)
#ant.addElement(element2)
print(ant)

cpt = Compute(101)
cpt.setAntenna(ant)
cpt.addBands(bands)
result = cpt.compute(11)
print(result)
print("frequency", result.frequencies[0].frequency)
azg = result.frequencies[0].getAzimuthGrid()
#print "azimuths", azg
elg = result.frequencies[0].getElevationGrid()
#print "elevations", elg
vals = result.frequencies[0].getMajorDbGrid()
#print "vals", vals
#for l in vals:
#    print l
analyzer = Analyzer(result)
analyzer.getRadiationPatternMax()
print("frontal gain", result.frequencies[0].getFrontalGain())
#print "radiated power", result.frequencies[0].getRadiatedPower()

#analyzer.getFigureOfMerit()
#ph = PlotHelper()
#ph.plot3d(azg, elg, vals)

#p = Population(Antenna, cpt)
#while True:
#	p.populationCycle()
