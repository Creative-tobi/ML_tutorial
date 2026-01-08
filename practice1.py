import practice2 as test #importing the whole file
from practice2 import check_for_bot #import only the needed function 
import sys #file path pyhtin check during importation
import random

# print ("Hello Ayodeji")


profile_data = [
    {"name": "Ade", 'age': 40, "bio": "Student loving python"},
    {"name": "ScamKing", 'age': 1, "bio": "I love coding"},
    {"name": "ElonMusk_Fake", 'age': 10, "bio": "Click link for CRYPTO giveaway"}
]

for user in profile_data:
    result = test.check_for_bot(user)
    print(f"Checking {user['name']}...{result}")




random_profile_data = random.choice(profile_data)
print(random_profile_data)
# print(sys.path)
# name = 'Aishat'
# print(name)
# greet = 'hi'

# #testing

# test = "Aishat is geek"
# print(len(test))
# print(test[4])
# print(test[0:9])


# practice = '{}, {}. I\'ve got this'.format(greet, name)

# print(practice)

# #LIST, TURPLE, SET
# #LIST METHOD 

# names = ['Shade', 'Ayodeji', 'Kammaldeen']
# names.append('Tobi')
# print(names)

# names.insert(1, 'Geek')
# names.sort()
# print(names)

# for items in names:
#     print(items)

# print(names.index('Geek'))

# #index, name and value using enum
# for index, call in enumerate(names):
#     print(index, call)


# #while for fibonacci series
# a,b = 0,1
# while a<10:
#     print(a)
#     a,b = b,a+b


# #if and if else statement
# '''x = int(input("Please enter an integer: "))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')'''    
    


# #if practice
# x = 10
# if x > 5:
#     print("Greater")
#     print("Done")

# weather = "Sunny"
# if weather == "Rainy":
#     print("Bring umbrella")

# '''x = 10
# if x > 5:
#    x > 20:
#         print("Big")
#         else:
#             print("Medium")
#             else:
#                 print("Small") '''
    


# #list of flight times
# flight_times = [0.08, 0.25, 0.05, 0.30, 0.09, 0.12]
# stress_count = 0

# for times in flight_times:
#     if times < 0.1:
#         print(f"Stress burst detected: {times}")
#         stress_count = stress_count + 1

#         print(f"Total stress burst found: {stress_count}")

# #using join of string 
# courses = ['geography', 'history', 'economics']

# course_str = " , ".join(courses)

# print(course_str)
# new_course_str = course_str.split(" , ")
# print(new_course_str)

# #turple make use of ()
# schools = ("Uniosun", "LAUTECH", "FUTMINNA")
# print(schools)

# # schools[0] = "UI" #error coz tuble is immutable
# # print(schools)

# print(str(type(schools))) #check type

# #SET unorderred collections without dublicate use {}
# schools = {"Uniosun", "LAUTECH", "FUTMINNA"}
# school_osun = {"Uniosun", "LAUTECH", "IrePoly"}
# print(schools.intersection(school_osun)) #common items
# print(schools.difference(school_osun)) #items in schools but not in school

# #empty list, set, tuple, dict
# empty_list = []
# empty_list2 = list()

# empty_tuple = ()
# empty_tuple2 = tuple()

# empty_set = {} #empty dict
# empty_set2 = set()

# print(dir(str)) #show availble methods for str
# #dictionaries work with key value like array

# student = {'name': 'Aishat', 'school': 'Uniosun', 'dept': ['compsci', 'maths']}
# print(student)
# print(student['dept'])



# #not existing key
# print(student.get('Kola'))
# print(student.get('Kola', 'Not found'))

# del student['school']

# #looping over key and value
# for key, value in student.items():
#     print(key, value)

import datetime
import calendar
import os
today = datetime.date.today()
print(today)

print(calendar.isleap(2025))

print(os.getcwd())
print(os.__file__)