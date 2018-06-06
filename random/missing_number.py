def main():
#given T test cases
#first line of test case is N
# second line is n-1 numbers\

#read in to solve as read in with counter
    t = int(input())
    for i in range(t):
        n = int(input())
        for i,num in enumerate(input().split(),1):
            if i != int(num):
                print(i)
                break

main()
