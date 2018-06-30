""" Reads in a list of call times, and outputs the number of minutes someone would be charged for those minutes under two different cell phone plans. 

Implements the solution to Problem 2 of the UIL District 2 2012 Programming Competition. 6/30/2018

"""
import math

def main():
    f = open("cell.dat", "r")
    aSum = 0
    bSum = 0
    for line in f:
        aSum += int(float(line))
        bSum += math.ceil(float(line))
    print ("PLAN A: " + str(aSum))
    print ("PLAN B: " + str(bSum))


if __name__ == "__main__":
    main()