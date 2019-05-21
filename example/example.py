from matplotlib import pyplot
import numpy as np
from fcutils import fcio

# The fcio class is used to open the datafile
io = fcio("th228.fcio")

print("Number of adcs", io.nadcs)
print("Number of samples", io.nsamples)

data = io.traces

start = 0
stop = 12 if io.nadcs > 12 else io.nadcs

#fig, axs = pyplot.subplots(2)

while io.next_event():
	if io.eventnumber > 10:
		break

	print("FlashCam: Event time: %f bl0: %d bl1: %d <bl>: %5.1f" %(io.eventtime,io.prebaselines0,io.prebaselines1,io.average_prebaselines))

	pyplot.plot(io.traces[0] - io.average_prebaselines[0], label="Trace %d" % io.eventnumber)

    	#for i, (bl, prebl0, integral, trace) in enumerate(zip(io.baselines, io.prebaselines0, io.integrals, io.traces)):
	#pyplot.plot(trace - bl, label="Trace %d" % io.eventnumber)

#axs[io.eventnumber].plot(trace - bl, label="Trace %d" % i)
#pyplot.ylim(190, 210)

pyplot.xlabel("Time [16 ns]")
pyplot.ylabel("Baseline subt. amplitude [LSB]")
pyplot.legend()
pyplot.show()
