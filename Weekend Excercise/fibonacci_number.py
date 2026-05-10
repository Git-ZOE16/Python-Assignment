#Fibonacci numbers is Adding the last two numbers to get the next one: e.g(0, 1, 1, 2, 3...)
#Pseudocode:
    #Step1. Start with 0 and 1.
    #Step2. Print the first, then update them to find the next.

a = 0
b = 1

for numbers in range(20):
    print(a)
    temp = a + b
    a = b
    b = temp
