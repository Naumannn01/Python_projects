#factorial using recursion

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))


#fibonacci series using recursion

a=int(input("Enter the number of series you want"))
def fibonacci(n):
    if n==0 or n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

for i in range (a):
    print(fibonacci(i))

