def main():
    x = input()
    t = c = g = s = 0
    for i in x:
        if i == "T":
            t += 1
        elif i == "C":
            c += 1
        else:
            g += 1
    if min(t,c,g) > 0:
        s = 7 * min(t,c,g)
    print(t**2 + c**2 + g**2 + s)

main()
