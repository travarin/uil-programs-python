""" Reads in info about the number of passengers boarding at each Bus stop, and calculates which section has the fewest passengers.

Implements the solution to problem 3 of the UIL District District 1 2012 Programming Competition. 6/19/2018

"""

def main():
    f      = open("bus.dat", "r")
    routes = int(f.readline())
    for i in range(routes):
        stops          = f.readline().split()
        passengers     = int(stops[0])
        sections       = ["A"]
        min_passengers = passengers
        for i in range(1, len(stops), 2):
            passengers += int(stops[i]) + int(stops[i+1])
            if passengers == min_passengers:
                sections.append(chr(i // 2 + 98))
            elif passengers < min_passengers:
                sections = [chr(i // 2 + 98)]
                min_passengers = passengers
        for section in sections:
            print (section.upper() + " ", end='')
        print (min_passengers)
    f.close()


if __name__ == "__main__":
  main()