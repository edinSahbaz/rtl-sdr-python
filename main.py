from ui import intro, sdr_setup, choose_mode
import numpy as np


def main():
    intro()
    sdr = sdr_setup()
    choose_mode(sdr)


if __name__ == '__main__':
    main()
