import requests
import json

def get_trivia_questions(amount=20, category=9, difficulty="medium", type="multiple"):
    """
    Function to retrieve trivia questions from the Open Trivia Database API.

    Parameters:
    - amount: Number of questions to retrieve.
    - category: The category of questions.
    - difficulty: The difficulty level of questions.
    - type: The type of questions.

    Returns:
    A list of dictionaries, each containing a trivia question.
    """
    base_url = "https://opentdb.com/api.php"
    params = {
        "amount": amount,
        "category": category,
        "difficulty": difficulty,
        "type": type
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = json.loads(response.text)
        return data["results"]
    else:
        print(f"Failed to retrieve questions. Status code: {response.status_code}")
        return []

def print_question_with_options(question):
    """
    Function to print a single trivia question with options.

    Parameters:
    - question: A single trivia question.
    """
    print(f"\nQuestion: {question['question']}")
    for i, option in enumerate(question['incorrect_answers'], start=1):
        print(f"{i}. {option}")
    print(f"{len(question['incorrect_answers']) + 1}. {question['correct_answer']}")

def ask_for_answer():
    """
    Function to get the user's answer and validate it.

    Returns:
    The user's answer as an integer.
    """
    while True:
        try:
            answer = int(input("Your answer (enter the number): "))
            if 1 <= answer <= 4:
                return answer
            else:
                print("Please enter a valid number (1-4).")
        except ValueError:
            print("Invalid input. Please enter a number.")

def evaluate_answer(user_answer, correct_answer):
    """
    Function to evaluate the user's answer against the correct answer.

    Parameters:
    - user_answer: The user's answer.
    - correct_answer: The correct answer.

    Returns:
    True if the answer is correct, False otherwise.
    """
    return user_answer == correct_answer

def main():
    """
    Main function to orchestrate the trivia game.
    """
    amount_of_questions = 20
    category_id_general_knowledge = 9
    difficulty_level_medium = "medium"
    question_type_multiple_choice = "multiple"

    questions = get_trivia_questions(
        amount=amount_of_questions,
        category=category_id_general_knowledge,
        difficulty=difficulty_level_medium,
        type=question_type_multiple_choice,
    )

    if not questions:
        print("No questions retrieved. Exiting.")
        return

    score = 0

    for index, question in enumerate(questions, start=1):
        print(f"\nQuestion {index}/{amount_of_questions}:")
        print_question_with_options(question)
        user_answer = ask_for_answer()
        correct_answer_index = len(question['incorrect_answers']) + 1

        if evaluate_answer(user_answer, correct_answer_index):
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print("\nGame Over!")
    percentage_correct = (score / amount_of_questions) * 100
    print(f"Your Score: {score}/{amount_of_questions} ({percentage_correct:.2f}% correct)")

if __name__ == "__main__":
    main()
