# To find the factorial of a number.
def factorial(n):
    if n<0:
        print("Factorial is not valid for negative numbers.")
        return None
    elif n>=2:
        return n*factorial(n-1)
    else:
        return 1
n=int(input("Enter a number: "))
result=factorial(n)

if result!=None:
    print("The factorial of",n,"is:",result)