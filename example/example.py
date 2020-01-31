from matplotlib import pyplot
import numpy as np
from fcutils import fcio

# The fcio class is used to open the datafile
io = fcio("./th228.fcio")

print("Number of adcs", io.nadcs)
print("Number of samples", io.nsamples)

data = io.traces

while io.next_event():
        if io.eventnumber > 10:
                break
        print("  Number of triggered adcs: ",io.numtraces,io.tracelist)
        for adc in io.tracelist:
                print("   FlashCam: ADC: %d Event time: %f bl0: %d <bl>: %d daq_e: %5.1f" %(adc,io.eventtime,io.prebaseline[adc],io.average_prebaseline[adc],io.daqenergy[adc]))
                pyplot.plot(np.array(io.traces[adc],dtype=np.int32)-io.average_prebaseline[adc], label="Trace %d - ch %d" %(io.eventnumber,adc))
                
pyplot.xlabel("Time [16 ns]")
pyplot.ylabel("Baseline subt. amplitude [LSB]")
pyplot.legend()
pyplot.show()
