""""
Student Grade Calculator
Author: Ebruphihor Blessing Okan
Date: September 7, 2025
Course: CST 205 100 - Introduction to Programming with Python
Description: Calculates per-student averages and letter grades,
             finds the top performer, and prints class statistics.
"""

print("Grade Calculator Program")

#Initialize dictionary Data 
#Keys = Student names: Vaules = List of grades (ints/floats)

students_grades = {
    "Blessing": [85, 90, 78], 
    "Anab": [92, 88, 95],
    "Efe": [70, 80, 82],
} 
print("Students and their grades:", students_grades)

#Helper function to calculate average using loop 

def average(numbers): 
    total = 0.0
    count =0 
    for n in numbers:  #Loop through each grade 
        total += n 
        count += 1
    if count > 0: 
        return total / count
    else:
        return 0.0


print("Average for Blessing:", round(average(students_grades["Blessing"]), 2)) 

# Calculate each per-student 

student_averages = {} #{name: average}

#Loop through each student in the dictionary
for name, grades in students_grades.items(): 
    student_averages[name] = average(grades) 
    
#Print Results 
print("Student averages:", student_averages) 


# Map numeric averages to letter grades using if/elif/else
# Store results in a new dictionary {student: letter grade}

def letter_grade(grade): 
    if 90 <= grade <= 100: 
        return "A"
    elif 80 <= grade < 90:
        return "B"
    elif 70 <= grade < 80:
        return "C"
    elif 60 <= grade < 70:
        return "D"
    else: 
        return "F" 
    
#Letter grade dictionary and loop through averages
student_letter_grades = {} #name: letter} 

for name, avg in student_averages.items():
    student_letter_grades[name] = letter_grade(avg) 
    
print("student letter grades:", student_letter_grades)

# Find top performer
top_student = None 
top_average = -1.0 

for name, avg in student_averages.items(): 
    if avg > top_average: 
        top_student = name 
        top_average = avg 
print(f"Top student: {top_student} with average {round(top_average, 2)}")

# Class statistics: overall average, highest, lowest
total_average = 0.0
count_average = 0

# Loop through all student average and add them up 
for avg in student_averages.values(): 
    total_average += avg   #add each student's average to total
    count_average += 1     # Increase the count of students
    
#avoid division by zero
if count_average > 0: 
    class_average = total_average / count_average
else: 
    class_average = 0.0 
    
#Count how many students passed (C or better)
pass_count = 0
for letter in student_letter_grades.values():
    if letter == "A" or letter == "B" or letter == "C":
        pass_count += 1
        

print("Class average:", round(class_average, 2))
print("Students with C or better:", pass_count, "/", len(student_averages))