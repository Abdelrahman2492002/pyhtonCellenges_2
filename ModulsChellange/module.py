from moduleChellange import chellange
import math
import random2

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Seconed Number: "))
operator = input("Enter Operator: ")

if operator == "+":
    print(chellange.sum(num1 , num2))

elif operator == "-":
    print(chellange.substraction(num1 , num2))

elif operator == "*":
    print(chellange.multiply(num1 , num2))

elif operator == "/":
    print(chellange.division(num1 , num2))

elif operator == "power":
    print(math.pow(num1 , num2))

elif operator == "sqr":
    print(math.sqrt(num1))

elif operator == "random":
    print(random2.randint(num1 , num2))

else:
    print("Please Enter valid Operator like (+ - * / pow sqr random)")