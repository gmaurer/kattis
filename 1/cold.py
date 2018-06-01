def main():
    x = int(input())
    temps = input().split()
    count = 0
    for i in range(x):
        if int(temps[i]) < 0:
            count += 1
    print(count)

main()
