""" Reads in a picture in portrait mode, and prints out the given picture rotated clockwise 90 degrees to landscape mode. 

Implements the solution to Problem 5 of the UIL District 2 2012 Programming Competition. 7/1/2018

"""
from itertools import islice

def main():
    f = open("family.dat", "r")
    cases = int(f.readline())
    for i in range(cases):
        picture = list(islice(f, 18))
        for col in range(len(picture[0])-1):
            for row in reversed(range(len(picture))):
                print (picture[row][col], end='')
            print ()
        print ()
        f.readline()
    f.close()

if __name__ == "__main__":
    main() 