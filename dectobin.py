n=int(input("Enter a number:"))
b=0
b2=bin(n)
print("The binary number is:",b2)
while(n>0):
    r=n%2
    b=(b*10)+r
    n=n//2
print("The binary no. is:",b)
