"""
Student Name: Marcelle Noukimi
Institution: Kennesaw State University
College: College of Computing and Software Engineering
Department: Department of Computer Science
Professor: Dr. Sarah North
Course Code & Title: CS 4308 Concepts of Programming Languages
                    Section 01 Fall 2021
Date: October 13, 2021

Assignment 3: Develop a Python program. Define a class in Python and use it to create an object
    and display its components. Define a Student class with the following components (attributes):
        	Name
        	Student number
        	Number of courses current semester
    This class includes several methods: to change the values of these attributes, and to display
    their values. Separately, the “main program” must:
        •	request the corresponding data from input and create a Student object.
        •	invoke a method to change the value of one of its attributes of the object
        •	invoke a method to that displays the value of each attribute.
"""
from Student import *

""""
    This is the main program to
    test Student class and view results
"""
# Instantiate a new student object
student = Student(None, None, None)

# Request the corresponding data from user input
student.StudentName = input("Enter the Student Name: ")
student.StudentNumber = input("Enter the Student Number: ")
student.NumberOfCourses = input("Enter the Student Number Of Courses you are taking this semester: ")
# Print Results
print("\nStudent details information\n", student.display())
# Ask the user if he may want to modify the value
# of one of the student attributes he just entered
choice = input("\nWould you like to change the value of one of its attributes? Yes/No ")

if choice == 'yes' or choice == 'Yes' or choice == 'YES':
    # if he enter 'yes' then he is prompted which student info value he would like to change
    # And enter into a loop that will run until the user decides not to continue to change value of its attributes
    while choice == 'yes' or choice == 'Yes' or choice == 'YES':
        # Then a menu option with a set of choice will be displayed with prompts
        print("Select the value you want to change")
        print(" If Student Name, Press 1")
        print(" if Student number, Press 2")
        print(" If Number of courses current semester, Press 3")
        ans = input("Your choice? ")
        if ans == '1':
            # if the user chooses option 1, it means he wants to change the value of the student name
            # The user is then asked to enter the new value of the student name
            newName = input("Enter the new value of the Student Name: ")
            # After entering the new value, we call the method setStudentName(self, name)
            # defined in the student class to change the value of the name of the student
            student.setStudentName(newName)
            # Print Results
            print("\nStudent details information\n", student.display())
        if ans == '2':
            # if the user chooses option 2, it means he wants to change the value of the student number
            # The user is then asked to enter the new value of the student number
            newNumber = input("Enter the new value of the Student Number: ")
            # After entering the new value, we call the method setStudentNumber(self, number)
            # defined in the student class to change the value of the student number
            student.setStudentNumber(newNumber)
            # Print Results
            print("\nStudent details information\n", student.display())
        if ans == '3':
            # if the user chooses option 3, it means he wants to
            # change the value of the courses he is taking the current semester
            # The user is then asked to enter the new value of the student number
            newCourses = input("Enter the new value of the Student Number of Courses taken the current semester: ")
            # After entering the new value, we call the method setStudentCourses(self, courses)
            # defined in the student class to change the value of the number of courses
            # taken this current semester
            student.setStudentNumberOfCourses(newCourses)
            # Print Results
            print("Student details information\n", student.display())

        # After modifying one value, the user is asked if he still want to make any modification
        choice = input("\nWould you like to change another value of its attributes? Yes/No ")
        # If he enters 'yes' then we enter in the loop again
        # else we exit the loop and then print the student value of each attribute (Student details information)
    print("\nStudent details information\n", student.display())

else:
    # Here we invoke the method display() defined in student class
    # to print the student value of each attribute (Student details information)
    print("\nStudent details information\n", student.display())
    exit()
