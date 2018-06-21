""" Determines the number of times the digit of a number must be added until the sum of the digits is nine or less. 

Implements the solution to Problem 4 of the UIL District 1 2012 Programming Competition. 6/20/2018

"""

def main():
    f = open("casting.dat", "r")
    nums = int(f.readline())
    for i in range(nums):
        num = f.readline()
        if find_sum(num[:-1]) <= 9:
            print (0)
        else: 
            print (find_degree(num[:-1], 1))
    f.close()

def find_sum(num):
    sum = 0
    for digit in num:
        sum += int(digit)
    return sum

def find_degree(num, degree):
    sum = find_sum(num)
    if sum <= 9:
        return degree
    else:
        return find_degree(str(sum), degree + 1)

if __name__ == "__main__":
  main()