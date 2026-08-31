# Student Marks Report Generator

A simple Python script that calculates a student's average marks across three distinct subjects (Backend, Frontend, and Design), assigns a letter grade based on that average, and outputs a formatted student report dictionary.

## Features
* **User Input:** Prompts for the student's name and marks for three core modules.
* **Average Calculation:** Automatically calculates the arithmetic mean of the provided scores.
* **Dynamic Grading:** Evaluates the average score against a standard grading scale (A to E).
* **Structured Output:** Aggregates all data points into a clean, structured Python dictionary format.

## Grading System Breakdown
The program determines the student's grade using the following criteria:

* **Grade A:** Average score of 80 or above.
* **Grade B:** Average score between 70 and 79.
* **Grade C:** Average score between 60 and 69.
* **Grade D:** Average score between 50 and 59.
* **Grade E:** Average score below 50.

## Prerequisites
* Python 3.x installed on your local machine.

## How to Run the Script
1. Clone or download this repository.
2. Open your terminal or command prompt.
3. Navigate to the project directory.
4. Execute the script using the following command:
   ```bash
   python main.py
   ```
5. Follow the on-screen prompts to input the student's name and academic scores.
