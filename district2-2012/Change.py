""" Determines how many ways a given amount of money can be paid using only pennies, nickels, dimes, quarters, and half-dollars.

Implements the solution to Problem 3 of the UIL District 2 2012 Programming Competition. 7/1/2018

"""

def main():
    coins = {0:50, 1:25, 2:10, 3:5, 4:1}
    f     = open("change.dat", "r")
    cases = int(f.readline())
    for i in range(cases):
        change = int(f.readline())
        print (find_combinations(change, 0, coins))
    f.close()

def find_combinations(change, coin, coins):
    if change == 0:
        return 1
    combinations = 0
    for i in range(coin, 5):
        if change >= coins.get(i):
            combinations += find_combinations(change-coins.get(i), i, coins)
    return combinations

if __name__ == "__main__":
    main()