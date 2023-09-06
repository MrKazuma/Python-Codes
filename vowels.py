s=str(input("Enter a string:"))
v=0
for i in s:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        v=v+1
print("No. of vowels in string are:",v)
