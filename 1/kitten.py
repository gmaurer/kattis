def main():
#original thought was to make a tree then just go till root is null and return the postorder_binary_depth_first_search
#after talking to friend it is much easier to invert the relationship to a 1 to 1 (a child has 1 parent)
    start = int(input())
    escape = []
    z = {}
    while True:
        y = [int(x) for x in input().split()]
        if y[0] is -1:
            break
        for i in y[1:]:
            z[i] = y[0]
    while True:
        escape.append(start)
        if z.get(start) == None:
            break
        start = z[start]
    print(*escape)

main()
