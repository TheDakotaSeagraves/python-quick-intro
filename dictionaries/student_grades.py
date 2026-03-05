student_grades = {}


# Function to add a student
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

# Function to display all students and grades
def display_Student():
    print("Student:")
    for name, grade in student_grades.items():
        print(f"{name}: {grade}")

# Function that updates student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"Student `{name}` grade updated to {grade}.")
    else:
        print(f"Student `{name}` not found.")       
       

# adding students
add_student("Dakota","C" )
add_student("Maggie", "A")
add_student("Kati", "A")
add_student("Magnus", "C")
add_student("Kayla", "B")
add_student("Damean", "D")
print("-----------------------")
#Displaying students and grades
display_Student()
print("-----------------------")
#Removing a student
remove_student("Damean")
print("-----------------------")
#Displaying students again
display_Student()
print("-----------------------")
update_student("Dakota", "B")
print("-----------------------")
print(student_grades)