import os

os.system("cls")
selection = input("Select math or converter to use the calculator or converter: (calc/conv) ")
if selection == "calc":
    os.system("python calc.py")
if selection == "conv":
    os.system("python conv.py")