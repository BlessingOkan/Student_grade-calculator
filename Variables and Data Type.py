'''
#Concatenation and Length Calculation

first_part = "Learning" 
second_part = "Python is fun!"
full_sentence = first_part + second_part
print(full_sentence) # Output: LearningPython is fun!



message = "Data Types" 
print(len(message)) # Output: 10 


#Variable Assignment and Data Types 
number_of_students = 30
year = 2025
current_balance = -500

#Basic Interger Operations
x = 10
y = 3

sum_val = x + y #13 
diff_val = x - y #7 
prod_val = x * y #30 
quotient = x / y #3.33333333333335 (a float)
floor_div = x // y #3 (an integer of division)
remainder = x % y #1 (Remainder of 10 divided by 3)
print(f"Sum: {sum_val}, Difference: {diff_val}, Product: {prod_val}, Quotient: {quotient}, Floor Division: {floor_div}, Remainder: {remainder}")

''' 

name = "Blessing"
age = 20
print(f"My name is {name} and I am {age} years old.")

# Examples of Boolean Assignment
is_student = True
has_access = False
is_valid_input = True

'''
- **Equal to:** `==`
- **Not equal to:** `!=`
- **Greater than:** `>`
- **Less than:** `<`
- **Greater than or equal to:** `>=`
- **Less than or equal to:** `<=`
'''

user_age = 18 
legal_driving_age = 16

can_drive = user_age >= legal_driving_age 
is_adult = user_age >= 18 
is_minor = user_age < 18 

print(f"Can the user Drive?: {can_drive}")
print(f"Is the user an adult? {is_adult}")
print(f"Is the user a minor? {is_minor}") 



my_text = "Hello World"
count = 100
pi_approx = 3.14
active = True

print(f"'{my_text}' is of type: {type(my_text)}")      # Output: 'Hello World' is of type: <class 'str'>
print(f"'{count}' is of type: {type(count)}")        # Output: '100' is of type: <class 'int'>
print(f"'{pi_approx}' is of type: {type(pi_approx)}")    # Output: '3.14' is of type: <class 'float'>
print(f"'{active}' is of type: {type(active)}")       # Output: 'True' is of type: <class 'bool'>

