def main():
    find = input().split()
    x = int(find[0])
    y = int(find[1])
    if y == 1:
        print(x*y)
    else:
        print((x*(y-1))+1)

main()
