def prm(n):
    c=0
    if(n<=1):
        return 0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if(c==2):
        return 1
    else:
        return 0

n=int(input("Enter a number:"))
if(prm(n)==1):
    print("The number is prime.")
else:
    print("The number is not a prime.")
