#Pseudocode
    #Step1. Initialize score to 0.
    #Step2. Loop 10 times (for 10 questions).
    #Step3. In each loop, generate two random numbers, A and B.
    #Step4. Ensure A is greater than or equal to B so the result is not negative.
    #Step5. Give the user 2 attempts to answer:
        #If correct: Add 1 to score, show "Correct!", and move to the next question.
        #If incorrect: Show "Try again" (if it's the first attempt) or show the correct answer (if it's the second).
    #Step6. After 10 questions, display the final total score.

import random

def generate_subtraction_problem():
    """Generates two numbers where the result is never negative."""
    number1 = random.randint(0, 20)
    number2 = random.randint(0, 20)
    
    
    if number1 >= number2:
        return number1, number2
    else:
        return number2, number1

def check_answer(number1, number2, user_answer):
    """Checks if the user's answer is correct."""
    return user_answer == (number1 - number2)

def run_app():
    print("--- Welcome to the Simple Arithmetic App ---")
    score = 0
    total_questions = 10

    for i in range(1, total_questions + 1):
        n1, n2 = generate_subtraction_problem()
        correct_answer = n1 - n2
        attempts = 2
        
        print(f"\nQuestion {i}: What is {n1} - {n2}?")
        
        while attempts > 0:
            try:
                guess = int(input("Your answer: "))
                if check_answer(n1, n2, guess):
                    print("Correct!")
                    score += 1
                    break
                else:
                    attempts -= 1
                    if attempts > 0:
                        print(f"Wrong. Try again! (Attempts left: {attempts})")
                    else:
                        print(f"Wrong. The correct answer was {correct_answer}.")
            except ValueError:
                print("Please enter a valid number.")

    print(f"\n--- Game Over ---")
    print(f"Your final score is: {score} out of {total_questions}")

if __name__ == "__main__":
    run_app()


