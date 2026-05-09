#Pseudocode:
    #Step1. Collect the first number.
    #Step2. Collect the second number.
    #Step3. Collect the operators (+, -, *, or /).
    #Step4. Use if statements to do the calculation based on the operator chosen.
    #Step5. print the result.


number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")


if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    result = number1 / number2
else:
    result = "Invalid Operator"

print("Result:", result)


