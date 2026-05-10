## 1. Sum of Multiples of 10 (1 to 20,000)

#Pseudocode
    #Step1. Initialize a variable total_sum to 0.
    #Step2. Loop through numbers from 1 to 20,000.
    #Step3. If a number is divisible by 10 (number % 10 == 0):
    #Step4. Add that number to total_sum.
    #Step5. Print the final total_sum.



total_sum = 0
for number in range(1, 20001):
    if number % 10 == 0:
        total_sum = total_sum + number

print("The sum is:", total_sum)
