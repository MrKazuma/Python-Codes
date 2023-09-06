n=int(input("Enter a binary number:"))
d=0
i=len(str(n))
while(n>0):
    r=n%10
    i=i-1
    d=d+(r*(2^i))    
    n=n//10
print("The decimal no. is:",d)
