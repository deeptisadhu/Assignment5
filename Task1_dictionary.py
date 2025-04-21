students_marks = {'Alice':85,'Mark':65,'Roni':90}
name = input("Enter student name: ")

if name in students_marks:
    print(students_marks[name])
else:
    print("Student not found")