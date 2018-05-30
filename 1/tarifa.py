def main():
    x = int(input())
    n = int(input())
    m = []
    total = 0
    for i in range(n):
        m.append(int(input()))
        total += (x- m[i])
    total += x
    print(total)

main()
