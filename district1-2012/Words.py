""" Reads in a list of Facebook names, and shortens them to be used in the game Words with Friends. 

Implements the solution to problem 12 from the UIL District 1 2012 Programming Competition. 6/14/2018

"""

def main():
    f = open("words.dat", "r")

    names = int(f.read(1))
    lines = f.readlines()
    for i in range(1, names+1):
        line = lines[i]
        name = line.split()
        result = name[0]
        for x in name[1:]:
            result += " " + x[0]
        print (result)


if __name__ == "__main__":
  main()