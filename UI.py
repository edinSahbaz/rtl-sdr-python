from rtlsdr import RtlSdr
from ASCII import antena


def show_ui():
    print('---------------------------------')
    print('| RTL-SDR Python implementacija |')
    print('---------------------------------')

    print(antena)

    serial_numbers = RtlSdr.get_device_serial_addresses()
    print('\nPronadjeni uredjaji (serijski brojevi):')
    print(serial_numbers, '\n')

    center_freq = float(input('Centralna frekvencija u MHz: ')) * 10e5
    bandwidth = float(input('Širina frekvencijskog pojasa u MHz: ')) * 10e5
    sample_rate = float(input('Širina uzorka u MHz: ')) * 10e5
    gain = float(input('Dobitak na prijemniku u dB: '))

    return_values = {
        'center_freq': center_freq,
        'sample_rate': sample_rate,
        'gain': gain,
        'bandwidth': bandwidth
    }

    return return_values
