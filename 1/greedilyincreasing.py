def main():
    x = int(input())
    y = [int(x) for x in input().split()]
    s = []
    inc = 0
    for i in range(len(y)):
        if y[i] > inc:
            inc = y[i]
            s.append(y[i])
    print(len(s))
    print(*s)


main()
