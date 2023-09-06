import array as arr
a=arr.array('i',[10,15,42,7,13,4,98,2,32,4,65])
p=int(input("Enter the position:"))
l=len(a)
print("The first array:")
for i in range(0,p):
    print(a[i],end=",")
print()
print("The second array:")
for i in range(p,l):
    print(a[i],end=",")
