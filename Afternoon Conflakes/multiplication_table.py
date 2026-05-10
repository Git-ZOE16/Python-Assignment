#Pseudocode
    #Step1. collect number from the user.
    #Step2. Loop from 1 to 10.
    #Step3. Multiply the user's number by the current loop number.
    #Step4. Print the result in the format: "Number x Loop = Result".


number = int(input("Enter a number for the table: "))

for value in range(1, 13):
    result = number * value
    print(number, "x", value, "=", result)
