""" Reads in a list of times for each swimmer, and prints out their fastest time. 

Implements the solution to Problem 7 for the UIL District 1 2012 Programming Competition. 6/17/2018

"""

def main():
    f = open("fastmile.dat", "r")
    swimmers = int(f.readline())
    for i in range(swimmers):
        line = f.readline().split()
        name = line[0]
        min  = line[1]
        for time in line[2:]:
             if time[:2] < min[:2] or time[:2] == min[:2] and (time[3:5] < min[3:5] or time[3:5] == min[3:5] and time[6:] < min[6:]):
                min = time
        print (name + " " + min)
    f.close()

if __name__ == "__main__":
  main()