
# 1. Write a function called "greeting" that prints "hello world" to the console
# def greeting():
#     print("hello world")

# 2. Execute (call/ run) the "greeting function"
# greeting()

# 3. Reduce this code using functions

# def print_info():
#     print("Shu")
#     print("Thomas")
#     print("Gustavo")
#     print("Alim")

# print("Day 1: Students in SRE class")
# print("lecture: git 101")
# print_info()


# print("Day 2: Students in SRE class")
# print("lecture: git 102")
# print_info()

# print("Day 3: Students in SRE class")
# print("lecture: python 101")
# print_info()


# 5. Nested Functions

# 6. Functions with parameters
# Create a function that creates the following recommendation letter.
# The Parameters for the functions should be the first and last name person you
# are recommending
# def create_rec_letter(last_name,first_name):
#     rec_letter = f"""
# Karen Jones
# 1234 Park St
# Anytown, Pennsylvania 12345

# April 14, 2019

# ABC College Admission's Board
# 1234 Butler Ave
# Everywhere, CA 12345

# Dear ABC College Admission's Board:

# My name is Karen Jones. I have served as a science teacher at Parktown High School for the past fifteen years and have had the privilege to serve as {first_name} {last_name}'s teacher for the past three. I have also been {first_name}'s advisor on the science academic team here at school. Due to his qualifications, I feel that {first_name} would be an excellent addition to your school.

# While he has been a student here, {first_name} has always challenged himself academically, taking all of the AP courses that our school has to offer. He has been captain of the academic team for the past two years, showing strong leadership qualities and organizational skills. His superior written and verbal skills have far surpassed any student of his age.

# {first_name} would bring much to your school, both in and out of the classroom. If you have any questions regarding {first_name}'s qualifications, please contact me at (123) 555-5555 or at Karen.Jones@email.com.

# Sincerely,


# Karen Jones
# Science Department Head
# Park Town High School"""
#     return rec_letter

# print(create_rec_letter("John", "Doe"))


# 7. Order of parameters
# In the last example, reverse the order of the arguments when the function is
# called (switch first name and last name) and look at the results


# 8 Write a function that accepts a List of numbers as an argument.
# Return a new List that includes the only the even numbers.
# nums = [1, 2, 3, 4, 5, 6]

# def even(numlist1):
#     newList = []
#     for number in numlist1:
#         if number % 2 == 0:
#             newList.append(number)
#     return newList

# print(even(nums))


# 9 Args and Keyword Args
# use the recommendation letter exercise and name your arguments
# def create_rec_letter(last_name,first_name):
#     rec_letter = f"""
# Karen Jones
# 1234 Park St
# Anytown, Pennsylvania 12345

# April 14, 2019

# ABC College Admission's Board
# 1234 Butler Ave
# Everywhere, CA 12345

# Dear ABC College Admission's Board:

# My name is Karen Jones. I have served as a science teacher at Parktown High School for the past fifteen years and have had the privilege to serve as {first_name} {last_name}'s teacher for the past three. I have also been {first_name}'s advisor on the science academic team here at school. Due to his qualifications, I feel that {first_name} would be an excellent addition to your school.

# While he has been a student here, {first_name} has always challenged himself academically, taking all of the AP courses that our school has to offer. He has been captain of the academic team for the past two years, showing strong leadership qualities and organizational skills. His superior written and verbal skills have far surpassed any student of his age.

# {first_name} would bring much to your school, both in and out of the classroom. If you have any questions regarding {first_name}'s qualifications, please contact me at (123) 555-5555 or at Karen.Jones@email.com.

# Sincerely,


# Karen Jones
# Science Department Head
# Park Town High School"""
#     return rec_letter

# print(create_rec_letter(last_name="Doe",first_name="John")

# Return statements break the code block
# Placement of Functions
# Local Scope
# Local Variables
# Do parameters and local variables have the same scope?
# Global Variables
# Global Variables and Local Variables with the Same Names


#### 1. Find the smallest number
# Write a function `smallest` that accepts a List of numbers as an argument.
# It should return the smallest number in the List.
# nums = [8,1, 2, 3, 4, 5, 6]
# def smallest(numList):
#     num1 = numList[0]
#     for i in numList:
#         if i< num1:
#             num1 = i
#     return num1
    
# print(smallest(nums))

#### 2. Find the largest number
# Write a function `largest` that accepts a List of numbers as an argument.
# It should return the largest number in the List.
# nums = [8, 1, 2, 3, 4, 5, 6,24]
# def max_num(numList):
#     num1 = numList[0]
#     for i in numList:
#         if i > num1:
#             num1 = i
#     return(num1)
# print(max_num(nums))

#### 3. Find the shortest String
# Write a function `shortest` that accepts a List of Strings as an argument.
# It should return the shortest String in the List.
# list = ["monday", "tuesday", "wednesday", "short"]
# def shortest_list(stringList):
#     newString = stringList[0] #short
#     for i in stringList:
#         if len(i) < len(newString):
#             newString = i
#     return newString
# print(shortest_list(list))

#### 4. Find the longest String
# Write a function `longest` that accepts a List of Strings as an argument.
# It should return the longest String in the List.
# list = ["monday", "tuesday", "wednesday", "this_is_the_longest"]
# def longest(strinList):
#     list2 = []
#     for i in strinList:
#         if len(i) > len(list2):
#             list2 = i
#     return list2
# print(longest(list))