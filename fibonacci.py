def fib(n):
    if(n<=1):
        return n
    else:
        return fib(n-1)+fib(n-2)
l=int(input("Enter a limit:"))
print("The fibonacci series for the following is :")
for i in range(0,l):
    print(fib(i),end=",")
