""" Determines the number of possible collisions given a word size and a hash code. 

Implements the solution to Problem 6 of the UIL District 2 2012 Programming Competition. 6/23/2018

"""

def main():
    f = open("hashcodes.dat", "r")
    cases = int(f.readline())
    for i in range(cases):
        line = f.readline().split()
        letters = int(line[0])
        code    = int(line[1])
        print (find_collisions(letters, code, 0))
    f.close()


def find_collisions(letters, code, prev):
    if letters == 0:
        return 1 if code == 0 else 0
    collisions = 0
    for letter in range(prev + 1, 27):
        collisions += find_collisions(letters - 1, code - letter, letter)
    return collisions

if __name__ == "__main__":
    main()