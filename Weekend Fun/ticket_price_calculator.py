#Pseudocode:
    #Step1. Collect the user's age.
    #Step2. Use if-elif-else statement to check which age bracket they fall into and assign the correct price string.



age = int(input("Enter your age: "))

if age < 5:
    print("Free")
elif age >= 5 and age <= 12:
    print("$5")
elif age >= 13 and age <= 64:
    print("$12")
else:
    print("$8")

