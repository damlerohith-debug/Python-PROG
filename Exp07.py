def factorial (n):
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def simple_interest(principal, time, rate =5.0):
    return (principal * time * rate) / 100

square = lambda x: x * x

n = int(input("Enter a number to calculate its factorial: "))
fact = factorial(n)
if fact is None:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial =", fact)

p = float(input("Enter principal amount: "))
t = float(input("Enter time in years: "))
print("Simple Interest(default rate 5%) =", simple_interest(p, t))

x = float(input("Enter a number to calculate its square: "))
print("Square =", square(x))

# mymath.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# use_mymath.py

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition =", add(a, b))
print("Subtraction =", subtract(a, b))
print("Multiplication =", multiply(a, b))
print("Division =", divide(a, b))