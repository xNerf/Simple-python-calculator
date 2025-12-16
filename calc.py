calc = input("Enter your first number here: ")
calc1 = input("Enter your second number here: ")
calc2 = input("Enter your math symbol here: ")
try:
    num1 = float(calc)
    num2 = float(calc1)
except ValueError:
    print("Error: Value isnt a number")

if calc2 == "+":
    calculated = num1 + num2
    calculated1 = int(calculated)
    print("The answer is: " + str(calculated1))
if calc2 == "-":
    calculated = num1 - num2
    calculated1 = int(calculated)
    print("The answer is: " + str(calculated1))
if calc2 == "*":
    calculated = num1 * num2
    calculated1 = int(calculated)
    print("The answer is: " + str(calculated1))
if calc2 == "/":
    calculated = num1 / num2
    calculated1 = int(calculated)
    print("The answer is: " + str(calculated1))