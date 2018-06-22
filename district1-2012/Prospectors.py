""" Reads in info for plots of land, and calculates how many acres are in each unclaimed plot of land. 

Implements the solution to Problem 10 of the UIL District 1 2012 Programming Competition. 

"""
from itertools import islice

def main():
    f = open("prospectors.dat", "r")
    sections = int(f.readline())
    for i in range(sections):
        section = list(islice(f, 8))
        used    = []
        for r in range(8):
            col = []
            for c in range(16):
                col.append(False)
            used.append(col)
        plots = []
        for row in range(8):
            for col in range(16):
                if section[row][col] == "*" and used[row][col] != True:
                    plots.append(find_plots(section, used, row, col))
        plots.sort(reverse = True)
        for plot in plots:
            print (str(plot) + " ", end='')
        print ()
        f.readline()
    f.close()

def find_plots(section, used, row, col):
    if section[row][col] != "*":
        return 0
    used[row][col] = True
    sum = 5
    if row > 0 and used[row-1][col] != True:
        sum += find_plots(section, used, row - 1, col)
    if col > 0 and used[row][col-1] != True:
        sum += find_plots(section, used, row, col - 1)
    if row < len(section) - 1 and used[row+1][col] != True:
        sum += find_plots(section, used, row + 1, col)
    if col < len(section[0]) - 2 and used[row][col+1] != True:
        sum += find_plots(section, used, row, col + 1)
    return sum


if __name__ == "__main__":
    main()