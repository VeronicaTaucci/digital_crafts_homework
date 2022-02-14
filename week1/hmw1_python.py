
# #* 1. Prompt the user for his name using the input function. Upon receiving their name, you will say hello to them.
# name = input("What is your name?")
# print(f"Hello, {name}!")

# * 2. Same as the first exercise, but this time print the user's name in ALL CAPS, and also tell them the number of letters in their name.
# name = input("What is your name?")
# print(f"Hello, {name.upper()}.!")
# if len(name) == 1:
#     print(f"Your name has one letter in it")
# else:
#     print(f"Your name has {len(name)} letters in it")
# #--created an if statement in case there is just one letter

# * 3. Madlib. Prompt the user for the missing words to a Madlib sentence using the input function.
# ____(name)____'s favorite subject in school is ____(subject)____.
# name = input("What is your name?")
# subject = input("What is your favorite subjec?")
# print(f"{name}'s favorite subject in school is {subject}")

# * 4. Day of the Week
# The user will enter a number from 0 to 6. Given this number, print a day of the week. 0 for Sunday, 1 for Monday, 2 for Tuesday, and so on.
# choice_day = int(input("What is the day?"))
# if choice_day == 0:
#     print("Sunday")
# elif choice_day == 1:
#     print("Monday")
# elif choice_day == 2:
#     print("Tuesday")
# elif choice_day == 3:
#     print("Wednesday")
# elif choice_day == 4:
#     print("Thursday")
# elif choice_day == 5:
#     print("Friday")
# elif choice_day == 6:
#     print("Saturday")
# else:
#     print("Day does not exist")

# * 5.Work or Sleep In? Prompt the user for a day of the week just like the previous problem. But this time, print "Go to work" if it's a work day and "Sleep in" if it's a weekend day.
# choice_day = int(input("What is the day?"))
# if choice_day == 0 or choice_day == 6:
#     print("Sleep in")
# elif choice_day > 0 and choice_day < 6:
#     print("Go to work")
# else:
#     print("Day does not exist")

# * 6. Celsius to Fahrenheit. Prompt the user for a number in degrees Celsius, and convert the value to degrees in Fahrenheit and display it to the user.
# Use the following formula: F = (C * 9/5) + 32
# celsius=int(input("Temperature in C?"))
# F = (celsius * 9/5) + 32
# print(f"{F} F")

# * 7. Using a while loop, print out the numbers between 1 and 10 inclusive, one on a line.
# i = 0
# while i<10:
#     i +=1
#     print(i)

# * 8. n to m Same as the previous problem, except you will prompt the user for the number to start on and the number to end on.
# i = int(input("What is the first number?"))
# j = int(input("What is the second number?"))
# while i<10:
#     print(i)
#     i+=1

# * 9. Print a Square. Print a 5x5 square of * characters. Example output:
# #  *****
# #  *****
# #  *****
# #  *****
# #  *****
# i = 0
# while i<5:
#     print("*"*5)
#     i+=1

# * 10. Print a Square II. Print a NxN square of * characters. Prompt the user for N.
# N = int(input("How big is the square?"))
# Y = 0
# while Y<N:
#     print("*"*N)
#     Y+=1

# * 11. Tip Calculator
# Your task is to write a program that calculates how much of a tip to leave at a restaurant.
# Prompt the user for two things: The total bill amount, The level of service, which can be one of the following: good, fair, or bad
# Calculate the tip amount and the total amount (bill amount + tip amount). The tip percentage based on the level of service is based on:
# good -> 20%
# fair -> 15%
# bad -> 10%

# bill_amount = float(input("Total bill amount? "))
# level_of_service = input("Level of service? ").lower().strip()
# if level_of_service == "good":
#     tip_amount = bill_amount * 0.2
# elif level_of_service == "fair":
#     tip_amount = bill_amount * 0.15
# elif level_of_service == 'bad':
#     tip_amount = bill_amount * 0.1
# total = bill_amount + tip_amount
# print("Tip amount: $%.2f" % tip_amount)
# print("Total amount: $%.2f" % total)

# * 2. Tip Calculator 2
# Allow the ability to divide the check into a equal parts amount a number of people. The user will enter the number of people to be divided amongst. Example session:
# bill_amount = float(input("Total bill amount? "))
# level_of_service = input("Level of service? ").lower().strip()
# split_ways = float(input("Split ways?"))
# if level_of_service == "good":
#     tip_amount = bill_amount * 0.2
# elif level_of_service == "fair":
#     tip_amount = bill_amount * 0.15
# elif level_of_service == 'bad':
#     tip_amount = bill_amount * 0.1
# total = bill_amount + tip_amount
# print("Tip amount: $%.2f" % tip_amount)
# print("Total amount: $%.2f" % total)
# print(f"Amount per person:${total/split_ways}")

# * 3.How many coins?
# Write a program that will prompt you for how many coins you want. Initially you have no coins. It will ask you if you want a coin? If you type "yes", it will give you one coin, and print out the current tally. If you type no, it will stop the program
# coin = 0
# answer=""
# while answer != "no":
#     print(f"you have {coin} coins")
#     coin+=1
#     answer = input("Do you want a coin?")
# print("Bye")

# solution:
# coin = 0
# answer = ''

# while answer != 'no':
#     print("You have {} coins".format(coin))
#     answer = input('Do you want another? ').lower()
#     if answer == 'yes':
#         coin+=1

# print('Bye')

#! 4. Print a Box --- need to make
# Given a height and width, input by the user, print a box consisting of * characters as its border. Example session:
# Width? 6
# Height? 4
# ******
# *    *
# *    *
# ******
# w = int(input("whidth?"))
# h = int(input("height?"))
# i = "*"+" "*h+"*"

# print("*"*w)
# print(i)
# print(i)
# print("*"*w)

# * 5. Print a Triangle. Print a triangle consisting of * characters like this:
#    *
#   ***
#  *****
# *******

# print("   *   ")
# print("  ***  ")
# print(" ***** ")
# print("*******")

# 5. Print a Tringle

# count = 1
# down = 3

# while count < 9:
#     print((down * " ") + (count * '*'))
#     down-=1
#     count+=2


# * 6. Multiplication Table. Print the multiplication table for numbers from 1 up to 10.
# i = 1
# while i <= 10:
#     j = 1
#     while j <= 10:
#         print(f"{j} X {i} = {i*j}")
#         j += 1
#     i += 1

#! Sum the Numbers. Create a list of numbers, print their sum.
# nums = [2, 3, 5, 7, 11, 13, 17]
# sum = 0
# for x in nums:
#     sum += x
# print(sum)
#! Largest Number. Create a list of numbers, print the largest of the numbers.
# nums = [2, 3, 5, 7, 11, 13, 17]
# max = 0
# for x in nums:
#     if(max < x):
#         max = x
# print(max)
#! Smallest Number. Create a list of numbers, print the smallest of the numbers.
# nums = [2, 3, 5, 7, 11, 13, 17]
# min = nums[0]
# for i in nums:
#     if i < min:
#         min = i
# print(min)


# #! 4. Even Numbers. Create a list of numbers, print each number in the list that is even.
# nums = [2, 3, 5, 7, 11, 13, 17,14,28]
# num = []
# for x in nums:
#     if x % 2 == 0:
#         num.append(x)
# print(num)

#! 5. Positive Numbers. Create a list of numbers, print each number in the list that is greater than zero.
# nums = [2, 3, 5, 7, 11, 13, 17,14,28, -14, -18]
# for i in nums:
#     if i > 0:
#         print(i)

#! 6. Positive Numbers II. Create a list of numbers, create a new list which contains every number in the given list which is positive
# * need to cast first
# nums = [2, 3, 5, 7, 11, 13, 17,14,28, -14, -18]
# pos_num = []
# for i in nums:
#     if i > 0:
#         pos_num.append(i)
# print(pos_num)

#!7. Multiply a list. Create a list of numbers, and a single factor (also a number), create a new list consisting of each of the numbers in the first list multiplied by the factor. Print this list.
# list1 = [2,6,8,12,45]
# list2=[2]
# list3=[]
# for i,j in zip(list1, list2):
#     list3.append(i*j)
#     print(list3)

#! 8. Reverse a String. Given a string, print the string reversed.
# string = "I am a little confused"
# i = 0
# while len(string)>i:
#     i -=1
#     append.string[i]

#! 1. Multiply Vectors
# list1 = [1, 3, 4, 6, 8]
# list2 = [4, 5, 6, 2, 10]
# list=[]

# for i,j in zip(list1,list2):
#     list.append(i*j)
# print(list)
# *----or-----
# list = []
# for i in range(0, len(list1)):
#     list.append(list1[i] * list2[i])
# print (str(list))

#! 2. Matrix Addition. Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is represented as an list of lists:
list1 = [[2, 2], [5, 3]]
list1 = [[3, 2], [7, 3]]
list3 = []

for i in range(list1)
