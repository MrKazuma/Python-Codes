import array as arr
a=arr.array('i',[1,2,5,6,4,5,8,5,5,6])
t=int(input("Enter the item to be found:"))
c=0
print(a.count(5))
for i in range(0,10):
    if(a[i]==t):
        c+=1
print("The frequency of ",t," is:",c)
