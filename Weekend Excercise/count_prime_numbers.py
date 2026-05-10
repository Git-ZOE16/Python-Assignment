#Pseudocode:
    #Step1. For every number, check for its prime number.
    #Step2. If true, it is prime.

count = 0

for numbers in range(2, 101):
    is_prime = True
    for value in range(2, numbers):
        if numbers % value == 0:
            is_prime = False
    if is_prime:
        print(numbers)
        count = count + 1


