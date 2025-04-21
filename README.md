# Assignment5

Task1


Features
Create a dictionary of student names and their marks
Prompt the user to enter a student's name
Display the marks if the student is found
Show a message if the student is not found
Requirements
Python 3.x
How to Run
Clone or download the repository.
Open a terminal or command prompt.
Navigate to the directory containing the Python file.
Run the program using:
bash
CopyEdit
python student_marks.py
Sample Code
python
CopyEdit
# student_marks.py

# Dictionary of student names and their marks
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88
}

# Prompt user for a student's name
student_name = input("Enter the student's name: ")

# Retrieve and display marks
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found.")
Example Output
rust
CopyEdit
Enter the student's name: Alice
Alice's marks: 85
rust
CopyEdit
Enter the student's name: John
Student not found.

Task2

Description
This Python program performs basic list operations including:
Creating a list of numbers from 1 to 10
Extracting the first five elements from the list
Reversing the extracted elements
Printing both the extracted list and the reversed list
It demonstrates fundamental Python list manipulation techniques like slicing and reversing.
Usage
To run the program, make sure you have Python installed (version 3.x recommended). Then execute the script from the command line or an IDE:
bash
CopyEdit
python script_name.py
Replace script_name.py with the name of your Python file.
Example Output
less
CopyEdit
Extracted list: [1, 2, 3, 4, 5]
Reversed list: [5, 4, 3, 2, 1]
Code Overview
python
CopyEdit
# Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Extract the first five elements
extracted = numbers[:5]

# Reverse the extracted list
reversed_extracted = extracted[::-1]

# Print the results
print("Extracted list:", extracted)
print("Reversed list:", reversed_extracted)
