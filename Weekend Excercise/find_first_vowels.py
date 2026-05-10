#Pseudocode:
    #Step1. Loop through each word and check their letter.
    #Step2. If it is a, e, i, o, or u, show its spot and stop.

word = "documents"
vowels = "aeiou"

for letters in range(len(word)):
    if word[letters] in vowels:
        print("Found at spot:", letters)
