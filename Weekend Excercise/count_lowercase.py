#Pseudocode:
    #Step1. Start count at 0.
    #Step2. If a letter is a small, add 1 to count.


word = "Documents, Experience"
count = 0

for x in word:
    if x.islower():
        count = count + 1
print(count)

