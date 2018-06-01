def main():
    z = []
    for x in range(5):
        y = input().split()
        d = list(map(int, y))
        e = sum(d)
        z.append(e)
    print(z.index(max(z)) + 1, max(z))

main()
