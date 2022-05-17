#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on May 2022
# This is a program that finds the average of 10 numbers

import random


def main():
    # This is the main function

    Counter = 0
    Counter2 = 0
    numbers_average = 0
    random_numbers = []

    for Counter in range(0, 10):
        random_number = random.randint(1, 100)
        random_numbers.append(random_number)
        print("The Random Number is: {0}".format(random_number))
    print("")

    for Counter2 in range(len(random_numbers)):
        numbers_average = random_numbers[Counter2] + numbers_average
    numbers_average = numbers_average / len(random_numbers)
    print("The Average is {0}".format(numbers_average))


if __name__ == "__main__":
    main()
