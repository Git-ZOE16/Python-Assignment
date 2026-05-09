#Pseudocode:
    #Step1. Enter the year.
    #Step2. Check if the year can be divided by 400. If yes, it is a leap year.
    #Step3. If not, check if it can be divided by 100. If yes, it is "not" a leap year.
    #Step4. If not, check if it can be divided by 4. If yes, it is a leap year.
    #Step5. If none are true, it is a regular year.




year = int(input("Enter a year: "))


if year % 400 == 0:
    print("This is a Leap Year")
elif year % 100 == 0:
    print("This is NOT a Leap Year")
elif year % 4 == 0:
    print("This is a Leap Year")
else:
    print("This is a regular Year")



