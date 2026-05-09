#Pseudocode:
    #Step1. Get two numbers (x and y) from the user.
    #Step2. Check if y is equal to 0.
    #Step3. If it is 0, print "Cannot divide by zero".
    #Step4. If it is not 0, divide x by y and print the result.



x = int(input("Enter first number (x): "))
y = int(input("Enter second number (y): "))


if y == 0:
    print("Cannot divide by zero")
else:
    result = x / y
    print(result)

