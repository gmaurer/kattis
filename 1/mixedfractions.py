def main():
    while True:
        y = [int(x) for x in input().split()]
        if y[0] is 0 and y[1] is 0:
            break
        print(y[0]//y[1], y[0]%y[1], "/",  y[1])



main()
