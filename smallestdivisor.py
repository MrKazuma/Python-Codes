n=int(input("Enter a number:"))
if(n%2==0):
    print("The smallest divisor is:2")
else:
    i=3    
    while(i<=n):
        if(n%i==0):
            print("The smallest divisor is:",i)
            break
        else:
            i=i+2
        
