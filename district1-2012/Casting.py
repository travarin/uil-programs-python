""" Determines the number of times the digit of a number must be added until the sum of the digits is nine or less. 

Implements the solution to Problem 4 of the UIL District 1 2012 Programming Competition. 6/20/2018

"""

def main():
    f = open("casting.dat", "r")
    nums = int(f.readline())
    for i in range(nums):
        num = f.readline()
        print (find_degree(num[:-1], True))
    f.close()

def find_degree(num, first):
    sum = 0
    for digit in num:
        sum += int(digit)
    if sum <= 9:
        return 0 if first else 1
    else:
        return find_degree(str(sum), False) + 1

if __name__ == "__main__":
  main()