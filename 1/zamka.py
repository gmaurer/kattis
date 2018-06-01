def main():
    l = int(input())
    d = int(input())
    x = int(input())
    y = []
    #good tip from a friend to go to first lowest and first highest instead of full list
    for i in range(l,d+1):
        total = 0
        for j in str(i):
            total += int(j)
        if total == x:
            y.append(i)
            break
    for i in reversed(range(l,d+1)):
        total = 0
        for j in str(i):
            total += int(j)
        if total == x:
            y.append(i)
            break
    print(y[0])
    print(y[1])

main()
