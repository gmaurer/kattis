def main():
    y = [int(x) for x in input().split()]
    z = [int(x) for x in input().split()]
    z = z[::-1]
    s = []
    solved = []
    s.append(y[0])
    for i in range(0,len(z)):
        s.append(z[i])
    s.append(0)
    for i in range(0,len(s)-1):
        for j in range(i+1,len(s)):
            t = s[i] - s[j]
            if not t in solved:
                solved.append(t)
    solved.sort()
    print(*solved)

main()
