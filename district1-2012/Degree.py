""" Reads in arrays of ints and deteremines the degree of each array. 

Implements the solution to Problem 6 of the UIL District 1 2012 Programming Competition. 6/18/2018

"""

def main():
    f = open("degree.dat", "r")
    cases = int(f.readline())
    for i in range(0, cases):
        nums = f.readline().split()
        degrees = 0
        for indx in range(len(nums)):
            current = int(nums[indx])
            for num in nums[indx+1:]:
                if int(num) < current:
                    degrees += 1
        print (degrees)
    f.close()

if __name__ == "__main__":
  main()