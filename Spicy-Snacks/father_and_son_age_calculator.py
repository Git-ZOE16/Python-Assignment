#Pseudocode:
    #Step1. collect input of the fathers age and the sons age.
    #Step2. Multiply the son's age by 2 and subtract it from the father's age.
    #Step3. If the result is negative, convert it to a positive number using the abs() function.
    #Step4. Print the result.



father_age = int(input("Enter father's age: "))
son_age = int(input("Enter son's age: "))


difference = father_age - (2 * son_age)


years = abs(difference)

print("The answer is:", years)



