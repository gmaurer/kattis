from decimal import *

def main():
    line = input()
    x = len(line)#use this as pointer to go from both sides of input, constant half time
    characters = {"whitespace":0, "upper":0, "lower":0, "symbol":0}
    for i in line:
        if i == "_":
            characters["whitespace"] += 1
        elif i.isupper():
            characters["upper"] += 1
        elif i.islower():
            characters["lower"] += 1
        else:
            characters["symbol"] += 1
    getcontext().prec = 6
    print('%.6f' % Decimal(characters["whitespace"]/x))
    print('%.6f' % Decimal(characters["lower"]/x))
    print('%.6f' % Decimal(characters["upper"]/x))
    print('%.6f' % Decimal(characters["symbol"]/x))

main()
