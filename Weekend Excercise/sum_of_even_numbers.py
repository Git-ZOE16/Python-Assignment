#Pseudocode:
    #Step1. Look at every digit in the number.
    #Step2. If number is even, add it to total.

number = 468
total = 0

for x in str(number):
    value = int(x)
    if value % 2 == 0:
        total = total + value

print(total)

