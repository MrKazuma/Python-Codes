a=[[1,5,3],
   [3,4,9],
   [8,7,6]]
b=[[6,5,3],
   [4,2,4],
   [7,1,2]]
s=[[0,0,0],
   [0,0,0],
   [0,0,0]]     
for i in range(0,3):
    for j in range(0,3):
        s[i][j] = a[i][j]+b[i][j]
print("The Sum of Above two Matrices is : ")
for i in s:
    print(i)
