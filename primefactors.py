def prm(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if(c==2):
        return 1
    else:
        return 0
n=int(input("Enter a number:"))
print("The prime factors of the number is:")
i=1
while(i<=n):
    if(n%i==0):
        if(prm(i)==1):
            print(i)
    i=i+1
    
