#Pseudocode:
    #Step1. Get weight and height.
    #Step2. Calculate BMI using the formula: BMI = weight / (height \times height).
    #Step3. Use conditional statements to print the category based on the BMI value.



weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))


bmi = weight / (height * height)

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Normal")
elif bmi >= 25 and bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")

