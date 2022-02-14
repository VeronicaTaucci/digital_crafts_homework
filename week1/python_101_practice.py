
# * 1. Hello You!. Prompt the user for his name using the input function. Example:
# name = input("What is your name?")
# print(f"Hello, {name}!")

# * 2. HELLO YOU!. Same as the first exercise, but this time print the user's name in ALL CAPS, and also tell them the number of letters in their name.
# name = input("What is your name?")
# print(f"HELLO, {name.upper()}!")
# if len(name) == 1:
#     print("YOUR NAME HAS ONE LETTER IN IT")
# else:
#     print(f"YOUR NAME HAS {len(name)} LETTERS IN IT! AWESOME")

# * 3. Madlib
# Prompt the user for the missing words to a Madlib sentence using the input function. You can make up your own Madlib sentence, but here's an example:____(name)____'s favorite subject in school is ____(subject)____.
# print("""
#     Please fill in the blanks below:
# ____(name)____'s favorite subject in school is ____(subject)____.
#     """)
# name = input("what is your name?")
# subject = input("What is your favorite subject?")
# print(f"{name}'s favorite subject in school is {subject}")

# * 4. Day of the Week
# Given the following code which prompts the user for a day number(Remember that the int function converts a numeric string to a number):

# print('Please enter a number from 0 - 6: ')
# day = int(input('Day (0-6)? '))
# if day == 0:
#     result = "Sunday"
# elif day == 1:
#     result = "Monday"
# elif day == 2:
#     result = "Tuesday"
# elif day == 3:
#     result = "Wednesday"
# elif day == 4:
#     result = "Thursday"
# elif day == 5:
#     result = "Friday"
# elif day == 6:
#     result = "Saturday"
# else:
#     result = "This number is not an option. Please select a number from 0 - 6: "

# print(result)


# * 5. Work or Sleep In?
# Prompt the user for a day of the week just like the previous problem. But this time, print "Go to work" if it's a work day and "Sleep in" if it's a weekend day. Example session:
# print('Please enter a number from 0 - 6: ')
# day = int(input('Day (0-6)? '))
# if day == 0 or day == 6:
#     result = "It's the weekend! Sleep in, baby!"
# elif day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
#     result = "It's the weekday! Go to work!"
# else:
#     result = "This number is not an option. Please select a number from 0 - 6: "
# print(result)

# * 6. Celsius to Fahrenheit
# Prompt the user for a number in degrees Celsius, and convert the value to degrees in Fahrenheit and display it to the user.
# C = int(input('Please enter the temperature (a number) in Celsius to convert the value to degrees in Fahrenheit: '))
# F = (C * 9/5) + 32
# print(F, "degrees F")

# * 7. Looping from 1 to 10
# Using a while loop, print out the numbers between 1 and 10 inclusive, one on a line.
# count = 0
# while count != 10:
#     count+=1
#     print(count)

# * n to m. Same as the previous problem, except you will prompt the user for the number to start on and the number to end on.
# print('Please enter a start number and an end number')
# start = int(input('Start from: '))
# end = int(input('End on: '))
# while start <= end:
#     print(start)
#     start+=1


# * Print a Square
# Print a 5x5 square of * characters.
# count = 0
# while count < 5:
#     print("*****")
#     count+=1


# * 10. Print a Square II. Print a NxN square of * characters. Prompt the user for N.
# num = int(input("How many stars?"))
# count = 1
# while count < num:
#     print("*"*num)
#     count +=1


# * 1. Tip Calculator
# Your task is to write a program that calculates how much of a tip to leave at a restaurant.
# Prompt the user for two things:
# The total bill amount
# The level of service, which can be one of the following: good, fair, or bad
# Calculate the tip amount and the total amount(bill amount + tip amount). The tip percentage based on the level of service is based on:
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

#! To format a float number as a dollar value, use Python's formatting syntax: "%.2f" % amount

# * 2. Tip Calculator 2. Allow the ability to divide the check into a equal parts amount a number of people. The user will enter the number of people to be divided amongst.
# bill_amount = float(input("Total bill amount? "))
# level_of_service = input("Level of service? ").lower().strip()
# num_split = int(input("Split how many ways?"))
# if level_of_service == "good":
#     tip_amount = bill_amount * 0.2
# elif level_of_service == "fair":
#     tip_amount = bill_amount * 0.15
# elif level_of_service == 'bad':
#     tip_amount = bill_amount * 0.1
# total = bill_amount + tip_amount
# split = total / num_split
# print("Tip amount: $%.2f" % tip_amount)
# print("Total amount: $%.2f" % total)
# print("Amount per persons: $%.2f" % split )


# * 3. How many coins? Write a program that will prompt you for how many coins you want. Initially you have no coins. It will ask you if you want a coin? If you type "yes", it will give you one coin, and print out the current tally. If you type no, it will stop the program. Example run:

# coin = 0
# answer = ""
# while answer !="no":
#     print(f"You have {coin} coins")
#     answer = input("Do you want a coin?").lower()
#     if answer == "yes":
#         coin +=1
# print("bye")


# * 4. Print a Box. Given a height and width, input by the user, print a box consisting of * characters as its border.

# count = 0
# width = int(input('Width? '))
# height = int(input('Height? '))
# print(width * "*")
# while count < height - 2:
#     print("*" + ((width - 2) * " ") + "*")
#     count +=1
# print(width * "*")

# * 5. Print a Triangle. Print a triangle consisting of * characters like this:

#    *
#   ***
#  *****
# *******
# count = 1
# down = 3

# while count < 9:
#     print((down * " ") + (count * '*'))
#     down-=1
#     count+=2

# * 6. Multiplication Table. Print the multiplication table for numbers from 1 up to 10

# num1 = 1
# num2 = 1
# while num1 <= 10:
#     while num2<=10:
#         print(f"{num1} X {num2} = {num1 * num2}")
#         num2+=1
#     num2 = 1
#     num1+=1
