def prm(n):
    c=1
    for i in range(1,n):
        if(n%i==0):
            c=c+1
    if(c==2):
        return 1
    else:
        return 0
l1=int(input("Enter lower limit:"))
l2=int(input("Enter upper limit:"))
print("The prime numbers btw the limit:")
for i in range(l1,l2):
    if(prm(i)==1):
        print(i)
