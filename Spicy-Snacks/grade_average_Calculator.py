#Pseudocode:
    #Step1. Collect three scores from the user.
    #Step2. Add the scores together and divide them by 3 to get the average.
    #Step3. Use if-elif-else statements to check which range the average falls into.
    #Step4. Print the letter grade.



score1 = int(input("Enter first score: "))
score2 = int(input("Enter second score: "))
score3 = int(input("Enter third score: "))


average = (score1 + score2 + score3) / 3


if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Average is:", average)
print("Letter Grade is:", grade)



