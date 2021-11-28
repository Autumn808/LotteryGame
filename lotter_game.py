"""
//Autumn Capasso
//Lab 2
//UMUC 300 SDEV
//March 19, 2020
This program to make a Pick 10 Value
"""
import random
import sys


def main():
    """ Lottery main"""

    # Initialize Selection Value
    selection = 0
    # This program will generate a pick 10 of random numbers that range between  0-9
    while selection < 3:
        # Display Menu
        print('Welcome to the Lottery Game')
        print('Main Menu')
        print('1. Pick 3 Lottery Number')
        print('2. Pick 4 Lottery Number')
        print('3. Exit Application')

        # Program takes in input
        print("Enter selection: ")
        selection = int(input())

        if selection == 1:
            """Selection for Pick3"""
            print(pick3())

        if selection == 2:
            """Selection for pick 4"""
            print(pick4())

        if selection == 3:
            end_program()

        else:
            """Invalid selection"""
            print("\r\n###############################6###############\r\n"
                  " * You have entered an invalid selection * "
                  " \r\n##############################################\r\n "
)


def pick3():
    """ Build (3) Digit Number"""
    pick3nums = str(random.randrange(0, 9)) + \
                str(random.randrange(0, 9)) + \
                str(random.randrange(0, 9))

    return "\r\n###############################\r\n# 3 Digit Value: " + \
           pick3nums + "  #\r\n###############################\r\n "


def pick4():
    """ Build (4) Digit Number"""
    pick4nums = str(random.randrange(0, 9)) + \
                str(random.randrange(0, 9)) + \
                str(random.randrange(0, 9)) + \
                str(random.randrange(0, 9))

    return "\r\n###############################\r\n# 4 Digit Value: " + \
           pick4nums + "  #\r\n###############################\r\n "


# Exit Function
def end_program():
    """ Will end program """
    sys.exit()


if __name__ == "__main__":
    main()
