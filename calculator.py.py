# calculator.py

def calculate(num1, operator, num2):
if operator == "+":
return num1 + num2
elif operator == "-":
return num1 - num2
elif operator == "*":
return num1 * num2
elif operator == "/":
if num2 != 0:
return num1 / num2
else:
return "Error: Cannot divide by zero!"
else:
return "Error: Invalid operator."

print("Welcome to Simple Calculator!")

while True:
try:
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

result = calculate(num1, operator, num2)
print("Result:", result)

except ValueError:
print("Please enter valid numbers.")

again = input("Do you want to calculate again? (yes/no): ")
if again.lower() != "yes":
print("Goodbye!")
break