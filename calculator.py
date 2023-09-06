def add(m,n):
    s=m+n
    return s
def sub(m,n):
    if(m>=n):
        s=m-n
    else:
        s=n-m
    return s
def mul(m,n):
    s=m*n
    return s
def div(m,n):
    if(m>=n):
        s=m/n
    else:
        s=n/m
    return s
m=int(input("Enter the first number:"))
n=int(input("Enter the second number:"))
print("Choose 1 for Addition.")
print("Choose 2 for Substraction.")
print("Choose 3 for Multiplication.")
print("Choose 4 for Division.")
print()
c=int(input("Enter your choice:"))
if(c==1):
    print("The result is:",add(m,n))
elif(c==2):
    print("The result is:",sub(m,n))
elif(c==3):
    print("The result is:",mul(m,n))
elif(c==4):
    print("The result is:",div(m,n))
else:
    print("Wrong Choice entered")
