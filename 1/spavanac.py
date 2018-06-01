def main():
    time = [int(x) for x in input().split()]
    hour = time[0]
    minute = time[1]
    if minute - 45 < 0:
        hour -= 1
        minute = 60 - (45 - minute)
    else:
        minute -= 45
    if hour < 0:
        hour = 23

    print(hour, minute)

main()
