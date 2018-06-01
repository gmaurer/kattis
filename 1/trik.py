def main():
    x = input()
    location = [1,0,0]
    for i in x:
        if i =="A":
            location[0], location[1] = location[1], location[0]
        elif i == "B":
            location[1], location[2] = location[2], location[1]
        else:
            location[0], location[2] = location[2], location[0]

    print(location.index(1)+1)

main()
