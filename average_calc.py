#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Dec. 14, 2022
# This program generates 10
# random numbers from 1 to
# 100 and calculates their
# average

import math
import random

def main():
    # introductory paragraph
    print("This program generates 10")
    print("random numbers from 1 to")
    print("100 and calculates their")
    print("average")
    print("")

    # initializing variables
    sum = 0
    random_num_list = []

    # generating numbers
    for counter in range(0, 10):
        random_num = random.randint(0, 100)
        random_num_list.append(random_num)
        # displaying generated number
        print("{} has been generated.".format(random_num))

    # updating sum
    for counter in range(0, 10):
        sum = sum + random_num_list[counter]

    # initializing avg
    avg = sum / 10

    # displaying results
    print("The average is {}.".format(avg))



if __name__ == "__main__":
    main()
