""" Reads in a list of distances a ship has traveled in nautical miles, and converts them to English miles (1 nautical mile = 1.15 English miles)

Implements the solution to Problem 9 of the UIL District 2 2012 Programming Competition. 7/5/2018

"""
import math

def main():
    f         = open("nautical.dat", "r")
    distances = int(f.readline())
    for i in range(distances):
        distance  = int(f.readline())
        english   = distance * 1.15
        english  *= 10
        lastDigit = english * 10 % 10
        english   = math.ceil(english) if lastDigit >= 5 else math.floor(english) 
        english  /= 10
        print (english)
    f.close()

if __name__ == "__main__":
    main()