#! https://digitalcrafts.instructure.com/courses/189/pages/lesson-working-with-numbers?module_item_id=23008

#* Calc Methods
# Write functions that accept two parameters, a and b, that print the result for each to the console

# add - print the result of a + b
# subtract - print the result of a - b
# multiply - print the result of a * b
# divide - print the result of a / b
# Call each one of your functions to make sure they work correctly.

# This function adds two numbers
# def calc_sum(a, b):
#     sum = a+b
#     return sum
# print(calc_sum(2, 3))

# # # This function subtracts two numbers
# def calc_sum(a, b):
#     sum = a-b
#     return sum
# print(calc_sum(2, 3))

# # # This function multiplies two numbers
# def calc_sum(a, b):
#     sum = a*b
#     return sum
# print(calc_sum(2, 3))

# # # This function divides two numbers
# def calc_sum(a, b):
#     sum = a/b
#     return sum
# print(calc_sum(2, 3))

##!-------------------------------------------------------------
###* 2 Pancake Calculator
## You need to calculate how many pancakes to make for a large con breakfast. Write a function that accepts two parameters: number of guests, number of pancakes per guest. The calculation for the total number of pancakes should be 12 % higher than the number of guests multiplied by the number of pancakes per guest, rounded up to the nearest whole number. Print the result to the console.
### Call your function to make sure it is working correctly. For example, 10 guests with 3 pancakes each = 34 pancakes total

# import math 
# def pancakes(guest_num,pancake_num):
#     total = guest_num * pancake_num
#     total1 = math.ceil((total* 12)/100)
#     total2 = total+total1
#     return(total2)
# print(pancakes(3,10))

##!-------------------------------------------------------------
##* Temperature Conversion
##Write a function called fahrenheitToCelsius that accepts a parameter for the temperature. Convert the temperature from celsius to fahrenheit and print the result. Do the opposite conversion in a function called celsiusToFahrenheit.
## F to C
# def fahrenheitToCelsius(temp):
#     result= temp - 32
#     return(result)
# print(fahrenheitToCelsius(50))

# ## C to F
# def celsius_to_F(temp):
#     result = (temp * 1.8)+32
#     return(result)
# print(celsius_to_F(50))

##!-------------------------------------------------------------
## need to come back and make the last 2 exercises
    
    