""" Reads in pictures in landscape mode, and outputs them rotated counter-clockwise 90 degrees to portrait mode. 

Implements the solution to problem 8 from the UIL District 1 2012 Programming Competition. 6/16/2018

"""
from itertools import islice

def main():
    f = open("landscape.dat", "r")
    pictures = int(f.readline())
    for i in range(0, pictures):
        picture = list(islice(f, 10))
        for col in range(14, -1, -1):
            for row in picture:
                print (row[col], end='')
            print ()
        print ()
        f.readline()


if __name__ == "__main__":
  main()