import math

def main():

    matches = [int(x) for x in input().split()]
    for i in range(matches[0]):
        match = int(input())
        x = matches[1]**2
        y = matches[2]**2
        hyp = math.sqrt(x+y)
        if match > hyp:
            print("NE")
        else:
            print("DA")


main()
