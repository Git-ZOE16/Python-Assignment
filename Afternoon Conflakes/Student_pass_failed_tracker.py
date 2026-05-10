#Pseudocode
    #Step1. Initialize pass_count and fail_count to 0.
    #Step2. Loop 15 times:
        # Enter a student score.
        # Convert the input to a number.
        # If the score is 45 or higher, add 1 to pass_count.
        # else, add 1 to fail_count.
    #Step3. Print the total number of passes and fails.
 
 
pass_count = 0
fail_count = 0

for i in range(1, 16):
    score = int(input("Enter score for student " + str(i) + ": "))
    if score >= 45:
        pass_count = pass_count + 1
    else:
        fail_count = fail_count + 1

print("Number of students who passed:", pass_count)
print("Number of students who failed:", fail_count)

