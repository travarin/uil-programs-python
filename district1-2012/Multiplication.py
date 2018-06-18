""" Reads in a list of multiplication problems, and prints out the subproducts and the final product for those problems. 

Implements the solution to problem 9 from the UIL District 1 2012 Programming Competition. 6/17/2018

"""

def main():
    f = open("multiplication.dat", "r")

    problems = int(f.readline())
    for problem in range(problems):
        nums = f.readline().split()
        r = int(nums[0])
        s = int(nums[1])
        for digit in reversed(nums[1]):
            print (str(r * int(digit)) + " ", end='')
        print (r * s)


if __name__ == "__main__":
  main()