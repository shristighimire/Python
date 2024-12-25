# -*- coding: utf-8 -*-
"""Python(Day49).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15L4bZZs1HpMbusB_qwW7rIvFB7FQJO95

1.  Create a function to read a list and look for words starting with a specific letter and remove them from the list. It could be any letter.
"""

def remove_words(words, letter):
  filtered_list = [word for word in words if not word.startswith(letter)]
  return filtered_list

"""2.  Run the function"""

words = ["cucumber", "strawberry", "apple", "orange", "banana"]
letter = "b"
result = remove_words(words, letter)

print("Original List:", words)
print(f"List after removing words starting with '{letter}':{result}")

"""3.  Develop a class of students with the following attributes: name, age, grade, school with default value "Marymount" and print a statement that emulates the following statement based upon your data: Mary is 15 and is in 11 grade at Marymount.   """

class Student:
    def __init__(self, name, age, grade, school="Marymount"):
        self.name = name
        self.age = age
        self.grade = grade
        self.school = school
    def print_student_info(self):
        print(f"{self.name} is {self.age} years old and is in Bachelor's {self.grade} at {self.school}.")

"""4.  Call the function"""

student01 = Student(name="Shristi", age=21, grade="3rd year")
student01.print_student_info()

"""5.  What would you do if you put the arguments in a different order than positional?"""

student01 = Student(grade="3rd year", age=21, name="Shristi")
student01.print_student_info()

"""5.5 Write an other function within class called Major.  Add major as parameter and print the major with the student's name when the function is called. In a separate code block call Major."""

class Student:
    def __init__(self, name, age, grade, school="Marymount"):
        self.name = name
        self.age = age
        self.grade = grade
        self.school = school
    def print_student_info(self):
        print(f"{self.name} is {self.age} years old and is in {self.grade}th grade at {self.school}.")
    def print_major(self, major):
        print(f"{self.name}'s major is {major}.")

student01 = Student(name="Shristi", age=21, grade=15)
student01.print_student_info()
student01.print_major(major="Computer Science")

"""Create a child class in the Students class called Athletes.  Have the function print "The student plays {q} sport."
"""

class Athlete(Student):
    def __init__(self, name, age, grade, sport, school="Marymount"):
        super().__init__(name, age, grade, school)
        self.sport = sport

    def print_sport(self):
        print(f"The student plays {self.sport} sport.")

"""6. Create an instance of a student and an athlete"""

athlete1 = Athlete(name="Shristi", age=17, grade=12, sport="Basketball")
athlete1.print_student_info()
athlete1.print_sport()

"""7.  Write a program to have an input of a number.  The input is passed to a function that squares the number and then adds 7 to the output.  The function will print the original input number and the number.
Make sure to put a flag to tell when you are done.
"""

def square_and_add_seven(number):
    result = number ** 2 + 7
    print(f"Original Input: {number}, Result: {result}")
while True:
    try:
        user_input = input("Enter a number (type 'done' to exit): ")
        if user_input.lower() == 'done':
            print("Program terminated.")
            break
        number = float(user_input)
        square_and_add_seven(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")