def main():
    x = int(input())
    s = 0
    for i in range(x):
        j = input()
        power = int(j[len(j)-1])
        num = int(j[0:len(j)-1])
        total = num**power
        s += total
    print(s)

main()
