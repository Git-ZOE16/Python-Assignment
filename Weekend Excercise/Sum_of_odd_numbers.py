#Pseudocode:
    #Step1. Look at every digit in the number.
    #Step2. If number is odd, add it to total.


number = 467531
total = 0

for y in str(number):
    value = int(y)
    if value % 2 != 0:
        total = total + value

print(total)

