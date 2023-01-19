from matplotlib.pyplot import *
from rtlsdr import *
from UI import show_ui
from operator import itemgetter

center_freq, sample_rate, gain, bandwidth = \
    itemgetter('center_freq', 'sample_rate', 'gain', 'bandwidth')(show_ui())

device_index = RtlSdr.get_device_index_by_serial('00000001')
sdr = RtlSdr(device_index)

# configure device
sdr.sample_rate = sample_rate
sdr.center_freq = center_freq
sdr.bandwidth = bandwidth
sdr.gain = gain

samples = sdr.read_samples(256*1024)
sdr.close()

# use matplotlib to estimate and plot the PSD
psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
xlabel('Frekvencija (MHz)')
ylabel('Relativna snaga (dB)')

show()
