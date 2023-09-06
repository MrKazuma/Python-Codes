def gcd(x,y):
    while (y):
        x,y=y,x%y
        return x
a=60
b=48
print(gcd(a,b))
