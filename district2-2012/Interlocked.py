""" Reads in three strings, and determines if every letter in the first two strings are contained in the third string in order, but not necessarily consecutively. 

Implements the solution to Problem 7 of the UIL District 2 2012 Programming Competition. 7/2/2018

"""

def main():
    f     = open("interlocked.dat", "r")
    cases = int(f.readline())
    for i in range(cases):
        words = f.readline().split()
        if check_interlocked(words[0], words[1], words[2]):
            print ("YES")
        else:
            print ("NO")
    f.close()

def check_interlocked(word1, word2, interlocked):
    indx1 = 0
    indx2 = 0
    for c in interlocked:
        if indx1 < len(word1) and word1[indx1] == c:
            indx1 += 1
        if indx2 < len(word2) and word2[indx2] == c:
            indx2 += 1
    return indx1 == len(word1) and indx2 == len(word2)

if __name__ == "__main__":
    main()