def arms(n):
    s=0
    p=n
    while(n>0):
        r=n%10
        s=s+(r**3)
        n=n//10
    if(s==p):
        return 1
    else:
        return 0
l=int(input("Enter the lower limit:"))
u=int(input("Enter the upper limit:"))
print("The armstrong numbers b/w these intervals:")
for i in range(l,u):
    if(arms(i)==1):
        print(i,end=',')
        
