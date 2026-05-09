### 5. Discount Eligibility
#Pseudocode:
    #Step1. Collect the bill amount and membership status.
    #Step2. Calculate the discount based on the two conditions.
    #Step3. Subtract the discount from the total and print the final results.


bill = float(input("Enter total bill: "))
member = input("Are you a member? (yes/no): ")

if bill >= 1000 and member == "yes":
    discount = bill * 0.10
    print("10% off")
elif bill >= 1000 and member == "no":
    discount = bill * 0.05
    print("5% off")
else:
    discount = 0
    print("No discount")

final_price = bill - discount
print("Final amount to pay:", final_price)

