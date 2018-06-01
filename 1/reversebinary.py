def main():
    x = int(input())
    y = to_reveresed_binary(x)
    print(to_int(y))

def to_reveresed_binary(x):
    rev_int = ""
    while x > 0:
        if x % 2 == 0:
            rev_int = rev_int + "0"
        else:
            rev_int = rev_int + "1"
        x //= 2
    return(rev_int)

def to_binary(x):
    rev_int = ""
    while x > 0:
        if x % 2 == 0:
            rev_int = "0" + rev_int
        else:
            rev_int = "1" + rev_int
        x //= 2
    return(rev_int)

def to_int(x):
    lng = len(x)-1
    total = 0
    for i in x:
        if i == "1":
            total += (2**(lng))
        lng -= 1
    return(total)


main()
