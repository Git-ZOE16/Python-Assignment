#Pseudocode:
    #Step1. Flip the number.
    #Step2. If the flip matches the start, it is a palindrome.

number = 121
text = str(number)
flip = text[::-1]

if text == flip:
    print("Yes")

