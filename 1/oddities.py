def main():
    #could just ask if even or odd from python
    #but doing it in the spirit of the problem
    #by using modulo to see if it returns 0 or 1
    x = int(input())
    for i in range(x):
        y = int(input())
        if y%2 == 0:
            print(y, " is even")
        else:
            print(y, " is odd")


main()
