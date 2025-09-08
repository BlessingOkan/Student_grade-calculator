# Student Grade Calculator

This project is a simple Python program that calculates student averages, assigns letter grades, finds the top performer, and prints overall class statistics.  

It was built as part of **CST 205 – Introduction to Programming with Python**.  

---

## Features
- Stores student grades in a **dictionary** (`{student: [grades]}`)
- Uses a **loop-based function** to calculate averages
- Assigns letter grades with **if/elif/else**
- Identifies the **top-performing student**
- Computes the **class average**
- Counts how many students received a grade of **C or better**

---

## How to Run

1. Clone this repository or download the ZIP.  
2. Open the folder in **VS Code** or any Python environment.  
3. Run the program from the terminal:

```bash
python3 grade_calculator.py-calculator

# Example Output 

Students and their grades: {'Blessing': [85, 90, 78], 'Anab': [92, 88, 95], 'Efe': [70, 80, 82]}
Average for Blessing: 84.33
Student averages: {'Blessing': 84.33, 'Anab': 91.67, 'Efe': 77.33}
Student letter grades: {'Blessing': 'B', 'Anab': 'A', 'Efe': 'C'}
Top student: Anab with average 91.67
Class average: 84.44
Students with C or better: 3 / 3
