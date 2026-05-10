#Pseudocode:
    #Step1. Keep dividing by 2.
    #Step2. Keep the remainders.

number = 10
result = ""

while number > 0:
    remainder = number % 2
    result = str(remainder) + result
    number = number // 2

print(result)
