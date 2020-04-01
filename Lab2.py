"""
//Autumn Capasso
//Lab 2 Math Program
//UMGC SDEV 300
//March 21,2020

This program will do math to make point to graph
"""

# Import for the math library and math functions.
from math import sin, pi, cos, sqrt, log
import numpy
import numpy as np

#this setter turns off  the divide warning of the log function
numpy.seterr(divide='ignore')


def main():
    """Lab 2 math main"""

    print('Select from the following options: ')
    print('1. Generates an x and sin(x) ')
    print('2. Generates x and cos (x)')
    print('3. Generates x and sqrt (x)')
    print('4. Generates x and log (x)')
    print(' 5. to exit program ')

    # Takes menu selection input
    MENU_SELECTION = int(input())

    # Generate the x and sin
    if MENU_SELECTION == 1:
        print('x and sin(x)')
        print("F(x), sin(x)")
        for x in np.arange(-2 * pi, 2 * pi, pi / 64):
            print(f'{x},{sin(x)}')

    # Generates the x and cos
    if MENU_SELECTION == 2:
        print('x and cos(x)')
        print("F(x), cos(x)")
        for x in np.arange(-2 * pi, 2 * pi, pi / 64):
            print(f'{x}, {cos(x)}')

    # Generates the x and sqrt
    if MENU_SELECTION == 3:
        print('x and sqrt(x)')
        print("F(x), sqrt(x)")
        for x in np.arange(0, 200 / 0.5):
            print(f'{x}, {sqrt(x)}')

    # Generates the x and log4
    if MENU_SELECTION == 4:
        print('x and log(x)')
        print("F(X), log(x)")
        for x in np.arange(0, 200, 0.5):
            print(f'{x}, {np.log(x)}')


if __name__ == "__main__":
    main()
