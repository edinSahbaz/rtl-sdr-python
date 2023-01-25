from ui import intro, check_devices, sdr_setup, choose_mode


def main():
    intro()
    devices_found = check_devices()

    if not devices_found:
        return

    sdr = sdr_setup()
    choose_mode(sdr)


if __name__ == '__main__':
    main()
