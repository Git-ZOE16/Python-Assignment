#Pseudocode:
    #Step1. Start with an empty ans.
    #Step2. Look at each letter in the word.
    #Step3. Put the letter at the front of reverse.


word = "Exercise"
reverse = ""

for x in word:
    reverse = x + reverse 

print(reverse)
