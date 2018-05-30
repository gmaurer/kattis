def main():
    x = int(input())
    y = int(input())
    #Improved by changing inner if statements to ternaries  
    if x > 0:
        print(1) if y > 0 else print(4)
#        if y > 0:
#            print(1)
#        else:
#            print(4)
    else:
        print(2) if y > 0 else print(3)
#        if y > 0:
#            print(2)
#        else:
#            print(3)


main()
