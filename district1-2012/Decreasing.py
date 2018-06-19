""" Reads in integers, and outputs the smallest multiple of that integer with digits in non-increasing order. 

Implements the solution to problem 5 from the UIL District 1 2012 Programming Competition. 6/15/2018

"""

def main():
    f = open("decreasing.dat", "r")
    cases = int(f.readline())
    for i in range(0, cases):
        base     = int(f.readline())
        multiple = base + base
        while not check_increasing(str(multiple)): 
            multiple += base
        print (multiple)
    f.close()

def check_increasing(num):
    prev = num[0]
    for c in num[1:]:
        if c > prev:
            return False
        prev = c
    return True

if __name__ == "__main__":
  main()