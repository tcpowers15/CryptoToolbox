"""
This program explores the way in which you can derive a row of DES S-Box 4 by using
another row
"""

import sys

def main():
    sbox4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
             [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
             [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
             [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]
    row = 0

    for col in range(16):
        val = sbox4[row][col]

        # flip the bits
        binary = bin(val)
        reversedBin = binary[-1:1:-1]
        reversedBin = reversedBin + (4 - len(reversedBin)) * '0'

        val = int(reversedBin, 2)
        val = val ^ 6

        newCol = 0

        for x in range(16):
            if sbox4[row][x] == val:
                newCol = x

        x  = newCol ^ 7


        if sbox4[row][col] != sbox4[3][x]:
            sys.exit("IT DOESNT WORK")

    print("It worked")
