def main():
    #wip
    #total factorial over number of each occurance factorial
    x = input()
    uniquesHigh = []
    uniquesLow = []
    for i in x:
        if i.isupper():
            if i not in uniquesHigh:
                uniquesHigh.append(i)
        else:
            if i not in uniquesLow:
                uniquesLow.append(i)
    y = len(uniquesLow) + len(uniquesHigh)
    print(factiorial(len(x)))

def factiorial(i):
    if i is 0:
        return(1)
    else:
        return( i * factiorial(i-1))

main()
