a=[[1,5,3],
   [3,4,9],
   [8,7,6]]
b=[[6,5,3],
   [4,2,4],
   [7,1,2]]
p=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            p[i][j]+=a[i][k]*b[k][j]
print("The product of Above two Matrices is : ")
for i in range(0,3):
    for j in range(0,3):
        print(p[i][j],end=',')
    print()
