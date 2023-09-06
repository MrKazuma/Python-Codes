b=input("Enter a binary no.")
def BinToDec(b):
    d=0
    for digit in b:
        d=d*2+int(digit)
    print(d)
BinToDec(b)
