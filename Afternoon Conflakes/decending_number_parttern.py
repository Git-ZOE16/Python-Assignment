#Pseudocode
    #Step1. Start a loop that begins at 5 and goes down to 1.
    #Step2. Inside that, start another loop that prints numbers from the current starting point down to 1.
    #Step3. Move to a new line after each inner loop finishes.

for numbers in range(5, 0, -1):
    for values in range(numbers, 0, -1):
        print(values, end="")
    print() 

