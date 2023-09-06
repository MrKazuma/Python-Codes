import math
def powoftwo(n):
    if(n==0):
        print("Invalid input")
    while(n>1):
        c=math.log2(n)    
        if(c.is_integer()==True):
            return 0
        else:
            return 1

n=int(input("Enter a number:"))
c=powoftwo(n)
if(c==0):
    print("Is power of 2")
elif(c==1):
    print("Not a power of 2")
            
