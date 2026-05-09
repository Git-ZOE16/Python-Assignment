#Pseudocode:
    #Step1. Collect user input for one letter.
    #Step2. Check if the input is actually a single letter from the alphabet using .isalpha().
    #Step3. If it is a letter, check if it is in the list of vowels: a, e, i, o, u.
    #Step4. If it's a letter but not a vowel, it's a consonant.
    #Step5. If it's a number or symbol, print "Invalid input".
 
 

letter = input("Enter one letter: ")


letter = letter.lower()


if letter.isalpha() and len(letter) == 1:
    
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        print("Vowel")
    else:
        print("Consonant")
else:
    # If it's a number, symbol, or more than one letter
    print("Invalid input")
