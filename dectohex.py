n=int(input("Enter a  number:"))
h=""
l=['A','B','C','D','E','F']
while(n>0):
    r=n%16
    if(r>=10):
        h=l[16-r]+h
    else:
        h=str(r)+h
        
    n=n//16
print("The hexadecimal number:",h)
