import array as arr
a=arr.array('i',[1,2,3,4,5,6,7,8,9,10])
a.reverse()
b=arr.array('i',reversed(a))
print("The reversed array:")
print(a)
print(b)
