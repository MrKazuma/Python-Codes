import array as arr
a=arr.array('i',[10,15,42,7,13,4,98,2,32,4,65])
max=0
min=0
for i in range(0,10):
    if(a[i]>max):
        max=a[i]
    if(min>a[i]):
        min=a[i]
print("The max :",max)
print("The min:",min)
