from . import geometry
from . import wires


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



ant = geometry.Geometry("Test antenna")


n = 0
for l,p in zip(lengths, positions):
    x = p
    y = l/2000.0
    z = 0
    start = (x,-y,z)
    end = (x,y,z)
    r = 0.005
    if n == 0:
        ant.addElement(wires.Wire(start, end, 0.005, "Reflector"))
    elif n == 1:
        ant.addElement(wires.ExcitedWire(start, end, 0.005, "Dipole", 0.5))
    else:
        ant.addElement(wires.Wire(start, end, 0.005, "Director%d"%(n-2)))
    n+=1

print(ant)

