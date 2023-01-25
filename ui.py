from rtlsdr import RtlSdr
from ASCII import antena
import asyncio
from power import streaming
from waterfall import show_waterfall


def intro():
    print('---------------------------------')
    print('| RTL-SDR Python implementacija |')
    print('---------------------------------')

    print(antena)


def check_devices() :
    serial_numbers = RtlSdr.get_device_serial_addresses()

    if len(serial_numbers) == 0:
        print('Spojite RTL-SDR uredjaj...')
        return False

    print('\nPronadjeni uredjaji:')
    print(serial_numbers, '\n')

    return True


def sdr_setup():
    center_freq = float(input('Centralna frekvencija u MHz: ')) * 10e5
    bandwidth = float(input('Širina frekvencijskog pojasa u MHz: ')) * 10e5
    sample_rate = float(input('Širina uzorka u MHz: ')) * 10e5
    gain = float(input('Dobitak na prijemniku u dB: '))

    device_index = RtlSdr.get_device_index_by_serial('00000001')
    sdr = RtlSdr(device_index)

    # configure device
    sdr.sample_rate = sample_rate
    sdr.center_freq = center_freq
    sdr.bandwidth = bandwidth
    sdr.gain = gain

    return sdr


def choose_mode(sdr):
    mode = input('\nWaterfall prikaz signala ili prikaz snage signala (w/s): ').lower()

    if mode == 'w':
        show_waterfall(sdr)
    elif mode == 's':
        asyncio.run(streaming(sdr))
    else:
        print('Pogresna opcija.')
