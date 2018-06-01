def main():
    n = int(input())
    while n > 0:
        total = 0
        buff = 0
        adjusted_hours = 0
        for i in range(n):
            speeds = [int(x) for x in input().split()]
            adjusted_hours = speeds[1] - buff
            total += (speeds[0] * adjusted_hours)
            buff = speeds[1]
        print(total, " miles")
        n = int(input())

main()
