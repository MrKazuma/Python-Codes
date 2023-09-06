def gcd(n,m):
    if(n>m):
        c=m
    else:
        c=n
    for i in range(1,c+1):
        if((n%i==0)and(m%i==0)):
            g=i
    return g
n=int(input("Enter first number:"))
m=int(input("Enter second number:"))
print("The GCD is:",gcd(n,m))
