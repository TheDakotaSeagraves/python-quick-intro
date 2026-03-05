# Initialize an empty dictionary of student grades
student_grades = {}

# Function to add a student and grade
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Student `{name}` added with grade {grade}.")

# Function to remove a student
def remove_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"Student `{name}` removed.")
    else:
        print(f"Student `{name}` not found.")

# Function to display all students and their grades
def display_students():
    print("Student Grades:")
    for name, grade in student_grades.items():
        print(f"{name}: {grade}")

# Function to update a student's grade
def update_grade(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"Student `{name}` grade updated to {grade}.")
    else:
        print(f"Student `{name}` not found.")       
    

# Add some students
add_student("Riley", "A")
add_student("Ellie", "B")
add_student("Milly", "C")
add_student("Rae", "A")
add_student("Beauregard", "D")
# Display students and their grades
display_students()
# Update a student's grade
update_grade("Beauregard", "B")
# Remove a student
remove_student("Beauregard")
# Display students and their grades again
print(student_grades)