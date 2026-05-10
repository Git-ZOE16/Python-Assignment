#Pseudocode
    #Step1. Get the height of a number from the user.
    #Step2. Loop from 1 up to the user's number.
    #Step3. In each step, print the star symbol (*) multiplied by the current loop number.

height = int(input("Enter the height of the triangle: "))

for i in range(1, height + 1):
    print("*" * i)

