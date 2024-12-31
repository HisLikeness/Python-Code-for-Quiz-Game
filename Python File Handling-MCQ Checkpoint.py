"""The Interactive Python Quiz Game is a text-based application that presents a series of multiple-choice questions to the user. The game provides instant feedback on each answer and keeps track of the user's score throughout the quiz. This project can be further enhanced with additional features such as random question order, a timer for each question, high score tracking, and a graphical user interface (GUI) using libraries like tkinter."""

import random
import json

def load_questions(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def display_question(question_data):

    print('\n', question_data["question"])
    for option in question_data["options"]:
        print(option)

    userInput = input("Enter your answer (A/B/C/D): ").upper()

    if userInput == question_data["answer"]:
        print("Correct!")
        return True
    else:
        print("Incorrect. The correct answer is:", question_data["answer"])
        return False


def play_quiz(questions):

    score = 0
    for question in questions:
        if input("Press Enter to continue...").lower() == 'q':
            break
        elif display_question(question):
            score += 1

    print("\nQuiz completed! Your score:", score, "/", len(questions))

# import the file containing the MCQ questions
if __name__ == "__main__":
    questions = load_questions("c:\\Users\\HP\\Documents\\STUDY\\DATA SCIENCE AND ANALYSIS - GOMYCODE\\Data Sets\\quiz_questions.json")
    random.shuffle(questions)
    play_quiz(questions)
