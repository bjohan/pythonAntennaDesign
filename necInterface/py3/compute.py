from necFileGenerator import *
from necFileParser import *
from simulationResult import *
import os;

class Compute:
        def __init__(self, rpres = 101):
                self.antenna = None
                self.bands = []
                self.rpres = rpres

        def addBands(self, bands):
                self.bands+=bands


        def setAntenna(self, antenna):
                self.antenna = antenna

        def compute(self, steps):
                try:
                        result = SimulationResult()
                        for band in self.bands:
                                print("Computing for", str(band))
                                result.append(self.computeBand(band, steps))
                        return result
                except:
                        print("Antenna died")
                        return None

        def computeBand(self, band, steps):
                #print "Generating geometry for", self.antenna.name
                fg = NecFileGenerator('output/test.nec')
                fg.comment(self.antenna.name)
                fg = self.antenna.addNecGeometry(fg)
                fg.geometryEnd()
                fg.end()
                fg.frequency(band.start, band.stop, steps)
                fg.radiationPattern(-180, 180, self.rpres, 0, 180, self.rpres)
                #print "Writing NEC file"
                fg.write()
                #print "Running NEC"
                os.system("nec2c -i output/test.nec -o output/test_output.dat")
                parser = NecFileParser("output/test_output.dat")
                return parser.simulationResult


