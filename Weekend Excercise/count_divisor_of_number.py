#Pseudocode:
    #Step1. Check every number from 1 up to a particular number.
    #Step2. If it divides perfectly (remainder 0), it is a divisor.
    

number = 10
count = 0

for value in range(1, number + 1):
    if number % value == 0:
        print("Divisor:", value)
        count = count + 1


