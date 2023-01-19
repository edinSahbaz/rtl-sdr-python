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

    center_freq = float(input('Unesite centralnu frekvenciju u MHz:\n')) * 10e5
    sample_rate = float(input('Unesite širinu uzorka u MHz:\n')) * 10e5

    return_values = {
        'center_freq': center_freq,
        'sample_rate': sample_rate
    }

    return return_values
