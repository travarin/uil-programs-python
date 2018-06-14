# 
# Travis Langston
# 6/14/2018
# 
# This is a solution to a problem from the UIL District 1 2012 Programming Competition. 
# It reads in a list of Facebook names, and shortens them to be used in the game Words With Friends. 
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