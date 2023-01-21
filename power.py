import asyncio
from matplotlib.pyplot import *


async def streaming(sdr):
    async for samples in sdr.stream():
        print(samples)
        psd(samples, NFFT=1024, Fs=sdr.sample_rate / 1e6, Fc=sdr.center_freq / 1e6)
        title(f'Snaga signala za frekvenciju od {sdr.center_freq / 1e6} MHz')
        xlabel('Frekvencija (MHz)')
        ylabel('Relativna snaga (dB)')
        show()

    # to stop streaming:
    await sdr.stop()

    # done
    sdr.close()
