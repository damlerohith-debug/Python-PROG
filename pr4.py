num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Addition=", num1 + num2)
print("Multiplication=", num1 * num2)
if num2 != 0:
    print("Division=", num1 / num2)
    print("Modulus=", num1 % num2)
    print("Floor Division=", num1 // num2)
else:    
    print("Division, Modulus, and Floor Division are not possible as the second number is zero.")
    print("Exponentiation=", num1 ** num2)