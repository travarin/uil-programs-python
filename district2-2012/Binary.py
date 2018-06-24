""" Reads in info about lights on a binary clock, and converts it to a base 10 format. 

Implements the solution to Problem 1 of the UIL District 2 2012 Programming Competition. 

"""
from itertools import islice

def main():
    f = open("binary.dat", "r")
    cases = int(f.readline())
    for i in range(cases):
        clock = list((islice(f, 4)))
        base_10 = ""
        for col in range(6):
            bin = ""
            for row in range(4):
                bit = clock[row][col]
                bin += bit if bit == "*" or bit == "o" else ""
            base_10 += binary_to_dec(bin)
        print (base_10[:2] + ":" + base_10[2:4] + ":" + base_10[4:])

def binary_to_dec(bin):
    exp = 1
    result = 0
    for bit in reversed(bin):
        result += exp if bit == "*" else 0
        exp *= 2
    return str(result)

if __name__ == "__main__":
    main()