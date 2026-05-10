#Pseudocode:
    #Step1. Declare a variable and assign numbers to the variable
    #Step2.Turn the number into text.
    #Step3. declare an empty string
    #Step4: put the text in front of the reverse word
 

number = 1234567890
text = str(number)

reverse = ""

for x in text:
    reverse = x + reverse

print(reverse)

