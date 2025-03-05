# Task 1: Calculate Factorial Using a Function

def factorial(a):
    if a < 2:
        return  1
    else:
        return a * (factorial(a-1))
num = int(input("Enter a number: "))
result = factorial(num)
print("Factorial of ",num, "is: ",result)