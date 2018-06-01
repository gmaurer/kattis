def main():
    hits = int(input())
    value = input().split()
    count = hits
    total = 0
    for x in range(count):
        if int(value[x]) >= 0:
            total += int(value[x])
        else:
            hits -= 1

    print(total/hits)

main()
