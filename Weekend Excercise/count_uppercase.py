#Pseudocode:
    #Step1. Start count at 0.
    #Step2. If a letter is a capital, add 1 to count.

word = "Documents, Independent, coLLAboration"
count = 0

for x in word:
    if x.isupper():
        count = count + 1

print(count)
