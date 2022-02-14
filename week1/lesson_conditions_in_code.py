
# * https://digitalcrafts.instructure.com/courses/189/pages/lesson-conditions-in-code?module_item_id=23010

# * Work or Sleep In
# Write a script that asks for a day of the week. If the day is a business day, print 'go to work!'. If the day is a weekend day, print 'sleep in!'. If whatever the user entered is not a day, print 'enter a valid day'.
# day = int(input("What day of the week is it?"))
# if day > 0 and day < 5: ##monday - day one
#     print("go to work")
# elif day == 6 or day == 7: ##saturday = 6, sunday = 7
#     print("sleep in")
# else:
#     print("enter a valid day")

# * Secret Password
# Write a script that asks the user for a password. If the user enters the correct word(pick one yourself) then print 'Welcome!', otherwise print 'Try Again!'
# password = "digital"
# guess = input("What is the password? ")
# if guess != password:
#     print("try again ")
# else:
#     print("welcome ")

# * Day of Week
# Write a script that asks the user for a number between 1-7. Print the corresponding day for the number, (i.e. 1='Sunday', 2='Monday' etc). If the input is invalid, print an error message.

# day = int(input("Please enter a number from 1 - 7:"))
# if day == 1:
#     result = "Sunday"
# elif day == 2:
#     result = "Monday"
# elif day == 3:
#     result = "Tuesday"
# elif day == 4:
#     result = "Wednesday"
# elif day == 5:
#     result = "Thursday"
# elif day == 6:
#     result = "Friday"
# elif day == 7:
#     result = "Saturday"
# else:
#     result = "This number is not an option. Please select a number from 1 - 7: "
# print(result)

# * Letter Grade
# Write a script that asks for a score number between 0-100. Print the corresponding grade for that number. (i.e. < 60=F, < 70=D, < 80=C, < 90=B, 90 += A). If the input is invalid, print an error message.
# score = int(input("What is the score 0-100? "))
# if score <60:
#     print("F")
# elif score < 70:
#     print("D")
# elif score < 90:
#     print("C")
# elif score < 90:
#     print("B")
# elif score >= 90:
#     print("A")

# * Picnic Game
# Write a function that returns true if the two input strings start with the same letter. Write a script that asks the user for their name. Ask them for the food they are bringing to the picnic. Use the function to check if the food matches the name. If it does, tell them they can come to the party. If it doesn't, tell them to try again.
# def match(name,food):
#     if name[0] == food[0]:
#         return True
# name = input("What is your name?")
# food = input("what are you bringing to the party?")
# if match(name,food)== True:
#     print("welcome")
# else:
#     print("try again")

# * Username length validator
# Write a function that accepts a parameter username, and checks if the username is valid. A valid username must be longer than 3 characters and less than 18. Use the function in a script that asks the user for a username and then tells them if the username is valid or not.
# def username(name):
#     if len(name.upper()) > 3 and len(name.upper()) < 18:
#         print("valid username")
#     else:
#         print("invalid username")
# name = input("what is the username?")
# username(name)

# * Odd and Divisible by 3
# Write a function that returns true if the input number is odd and divisible by 3. Write a script that asks the user for a number, then pass that number to the function and print a success message if the function returns true.
# def odd(num):
#     if num % 2 != 0 and num % 3 == 0:
#         return True
# num = int(input("What is the number? "))
# if odd(num) == True:
#     print("succes")
# else:
#     print("not odd or devisible by 3")
