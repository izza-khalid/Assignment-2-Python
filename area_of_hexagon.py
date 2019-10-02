#!/usr/bin/env python3

# Created by: Izza Khalid
# Created on: Sep 2019
# This program calculates the area of a hexagon
#     with user input

import math


def main():
    # this function calculates the area of a hexagon

    # input
    lengthofside = int(input("Enter the length of a side of a hexagon (mm): "))

    # process
    area_of_hexagon = ((3 * math.sqrt(3) * (lengthofside * lengthofside)) / 2)

    # output
    print("")
    print("Area is: {0:,.2f} mm^2".format(area_of_hexagon))


if __name__ == "__main__":
    main()
