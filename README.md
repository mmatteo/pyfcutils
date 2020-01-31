At the moment pyfcutils offers a wrapper around the fcio library, with simplified accessors to the config and event data.

This library is work in progress.
If and when a stable state should be reached, it will probably be merged into the fc-utils repository.

You need cython to compile the library, which can be installed through the usual channels like:

```
pip install -e pyfcutils
```

or

```
pip install cython
```

or

```
conda install cython
```

This depends of course on your setup.

To build and install the library a

```
make install
```

is sufficient. There will probably be a warning about a deprecated numpy 1.7 API call. This is a feature of cython and can be ignored.

The example.py file show you how to easily display FlashCam waveforms and related data (timestamp, baseline estimate, ...)

```
python example.py
```

The fcio class provides the following accessors to the FCIOConfig members:
```
nsamples # samples per channel
nadcs # number of adc channels
ntriggers # number of triggertraces
telid # id of telescope
adcbits # bit range of the adc channels
sumlength # length of the fpga integrator
blprecision # precision of the fpga baseline
mastercards # number of attached mastercards
triggercards # number of attached triggercards
adccards # number of attached fadccards
gps # gps mode (0: not used, 1: external pps and 10MHz)
```

The FCIOEvent accessors are the following
```
numtraces # number of adcs that have triggered for each events
tracelist # list of triggered adc channels
traces # the full traces for the event, shape = (nadcs, nsamples)
daqenergy # the fpga energy values for each channel in LSB
prebaseline # the fpga baseline values for each channel in LSB
eventnumber # the eventnumber since the beginning of the file
eventtime # the time since the beginning of the file in seconds
```

the traces / triggertraces members are numpy arrays wrapped around the fcio memory field, and provide a shape member, whichs corresponds to (nadcs,nsamples) or (ntriggers,nsamples)
