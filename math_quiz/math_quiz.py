# math_quiz/quiz.py
import random

def generate_integers(min_value, max_value):
    """
    Generates a random integer within the given range.
    """
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Generates a random arithmetic operator (+, -, *).
    """
    return random.choice(['+', '-', '*'])


def execute_operation(num1, num2, operator):
    """
    Performs the specified arithmetic operation on two numbers.
    Returns a tuple containing the problem string and the correct answer.
    """
    
    problem = f"{num1} {operator} {num2}"
    if operator == '+': result = num1 + num2
    elif operator == '-': result = num1 - num2
    else: result = num1 * num2
    return problem, result


def math_quiz():
    """
    Conducts a math quiz game with three questions.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_integers(1, 10)
        num2 = generate_integers(1, 5)
        operator = generate_random_operator()

        problem, answer = execute_operation(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            user_answer = 0  # Assigning a default value in case of an error

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()