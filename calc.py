import os
os.system("cls")
basevalue = 0
print("Welcome to the calculator!")
print("You can do addition (+), subtraction (-), multiplication (*), division (/), and percentage (%), and exponentiation (**).") 
calc = input("Enter your first number here: ")
calc1 = input("Enter your second number here: ")
calc2 = input("Enter your math symbol here: ")
if calc2 == "%":
    basevalue = input("Type the base value here: ")
try:
    num1 = float(calc)
    num2 = float(calc1)
    num3 = float(basevalue)
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
if calc2 == "%":
    calculated = (num1 / num2) * (num3)
    calculated1 = int(calculated)
    print("The answer is: " + str(calculated1) + "%")     
if calc2 == "**":
    calculated = num1 ** num2
    calculated1 = int(calculated)
    print("The answer is: " + str(calculated1))     