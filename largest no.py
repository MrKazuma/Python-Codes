def great(a,b,c):
    if(a>b):
        if(a>c):
            return a
        else:
            return c
    else:
        if(b>c):
            return b
        else:
            return c
a=int(input("Enter the 1st no.:"))
b=int(input("Enter the 2nd no.:"))
c=int(input("Enter the 3rd no.:"))
print("The largest of three nos is:",great(a,b,c))
