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

"""
   This is the Student class with its components (attributes): 
    	Name 
    	Student number 
    	Number of courses current semester 
   and the several methods to change the values of these attributes, 
   and to display their values.
"""


class Student:
    """
    Implementation of student class
    """

    def __init__(self, name, studentNumber, numberOfCourses):
        """
        Constructor. Each student holds a Name, a Student number,
        and a number of courses that he/she is taken during
        this semester
        """

        # Name of the student
        self.StudentName = name
        # Student number
        self.StudentNumber = studentNumber
        # Number of courses current semester

        self.NumberOfCourses = numberOfCourses

    """
    Various setter methods
    """

    # Method to change the value of a student name
    def setStudentName(self, name):
        self.StudentName = name

    # Method to change the value of a student number
    def setStudentNumber(self, number):
        self.StudentNumber = number

    # Method to change the value of a student number of courses
    # for the current semester
    def setStudentNumberOfCourses(self, courses):
        self.NumberOfCourses = courses

    """
    Method to display the value of each attribute of a student 
    """
    def display(self):
        # Print student details information
        return "Student Name: " + self.StudentName + "\n Student Number: " \
               + self.StudentNumber + "\n Number Of Courses taken the current semester: " + self.NumberOfCourses
