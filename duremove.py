import array as arr
a=arr.array('i',[1,2,3,3,4,4,4,5,6,7])
for i in a:
    if(a.count(i)>1):
        a.remove(i)
for i in a:
    print(i)
