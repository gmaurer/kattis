def main():
    x = input().split()
    correct = [1,1,2,2,2,8]
    fix = [0,0,0,0,0,0]

    for i in range(6):
        adjust = int(x[i])-correct[i]
        if adjust < 0:
            fix[i] = abs(adjust)
        elif adjust > 0:
            fix[i] = -adjust
    print(*fix)

main()
