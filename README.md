# IEEE LGU AI/ML Cohort One — Week 1 Assignment

**Name:** Zainab Saeed
**Roll No:** 238
**Projects Chosen:** Option 1 (Number Guessing Game) & Option 2 (Student Grade & Attendance Tracker)

## Project Descriptions

### 1. Number Guessing Game (`task1_number_guessing/number_guessing.py`)
A console game where the computer randomly picks a secret number and the player tries to guess it within a limited number of tries. The player first chooses a difficulty level (Easy, Medium, or Hard), which sets the number range and the number of allowed attempts. After each guess, the game gives a "Too High" or "Too Low" hint and shows the remaining attempts. If the player guesses correctly, they earn a score based on how quickly they guessed it; otherwise, the secret number is revealed. The player can choose to play again at the end.

### 2. Student Grade & Attendance Tracker (`task2_student_tracker/student_tracker.py`)
A program that collects a student's name and roll number, then takes marks for at least 3 subjects (stored using dictionaries). It calculates the average score and assigns a letter grade (A, B, C, or F) based on standard grading bands. It also asks for the total classes held and classes attended to calculate the attendance percentage, and checks whether the student meets the minimum 75% attendance requirement. Finally, it prints a clean report card with all of this information, including exam eligibility status.

## How to Run

Make sure you have Python 3.8+ installed, then run each project from the repository's root folder:

```bash
python task1_number_guessing/number_guessing.py
```

```bash
python task2_student_tracker/student_tracker.py
```

## Screenshots

See the `screenshots/` folder for terminal output showing:
- `task1_output.png` — a successful run and an invalid-input case for the Number Guessing Game.
- `task2_output.png` — a successful run of the Student Grade & Attendance Tracker.


## Notes

- Both programs are written in pure Python (no third-party libraries) and include input validation so they don't crash on invalid input.
- Code is organized into small, well-named functions with comments explaining each step.
