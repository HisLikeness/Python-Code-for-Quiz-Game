# Python-Code-for-Quiz-Game
This project implements a text-based **Quiz Game** in Python. The game presents multiple-choice questions to the user, tracks their score, and provides feedback on each answer.

## Features
- **Multiple-choice Questions**: The game displays a set of multiple-choice questions.
- **Instant Feedback**: Users receive immediate feedback on their answers.
- **Score Tracking**: The game keeps track of the user's score throughout the quiz.
- **Dynamic Question Order**: The order of the questions is shuffled randomly each time the game is played.
- **Exit Option**: Users can exit the game at any point by pressing 'q'.

## How It Works
### Key Functions
1. **`load_questions(filename)`**:
   - Loads questions from a JSON file.
   - The JSON file must contain a list of questions, each with a `question`, `options` (list of answers), and the `answer` (correct option).

2. **`display_question(question_data)`**:
   - Displays the question and its multiple-choice options.
   - Accepts user input for the answer and provides feedback on whether it was correct or not.

3. **`play_quiz(questions)`**:
   - Shuffles the questions and iterates through them.
   - Tracks the user's score and ends the quiz once all questions are answered or if the user chooses to quit.

### Example of the `quiz_questions.json` Format
Your questions file (`quiz_questions.json`) should look something like this:

```json
[
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
        "answer": "B"
    }
]
```

### Sample Gameplay
```plaintext
Press Enter to continue...
What is the capital of France?
A) Berlin
B) Madrid
C) Paris
D) Rome
Enter your answer (A/B/C/D): C
Correct!

Press Enter to continue...
What is 2 + 2?
A) 3
B) 4
C) 5
D) 6
Enter your answer (A/B/C/D): B
Correct!

Quiz completed! Your score: 2 / 2
```

## How to Run the Game
1. Clone or download this repository.
2. Ensure you have a `quiz_questions.json` file formatted correctly (refer to the example above).
3. Run the script:
   ```bash
   python quiz_game.py
   ```

### Exiting the Game
To exit the quiz at any time, press `q` when prompted to continue.

## Enhancements
This project can be extended with additional features such as:
- **Timer**: Limit the time for each question.
- **High Score Tracking**: Keep track of the highest score across multiple game sessions.
- **Graphical User Interface (GUI)**: Use libraries like `tkinter` to create a graphical interface for the quiz.
- **Random Question Order**: Shuffle the questions to make each game session unique.

## Contributions
Feel free to contribute by:
- Adding more questions or categories.
- Implementing new features such as a timer or high score tracking.
- Improving error handling or code performance.

---

Enjoy the quiz! 😄
```
