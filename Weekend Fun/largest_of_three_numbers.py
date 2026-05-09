#Pseudocode:
#Step1. Collect three inputs (a, b, and c).
#Step2. Assume the first input (a) is the largest.
#Step3. Use an if statement to check if b is bigger than the current largest (a); if yes, update it.
#Step4. Use another if statement  to check if c is bigger than the current largest (b); if yes, update it.



a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))


largest = a

if b > largest:
    largest = b


if c > largest:
    largest = c

print("The largest is:", largest)

