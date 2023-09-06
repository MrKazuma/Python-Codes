n=int(input("Enter the range for pattern:"))
p=0
for i in range(0,n):
    for j in range(0,p):
        print(end=' ')
    p=p+1
    for k in range(0,n-i):
        print('*',end=' ')
    print()
