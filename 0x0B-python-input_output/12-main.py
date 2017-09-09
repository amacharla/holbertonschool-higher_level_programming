#!/usr/bin/python3
Student = __import__('12-student').Student

student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json() # no attr specified
j_student_2 = student_2.to_json(['first_name', 'age']) # get first_name and age
j_student_3 = student_2.to_json(['middle_name', 'age']) # get age and not middle man because it doesnt exist

print(j_student_1)
print(j_student_2)
print(j_student_3)
