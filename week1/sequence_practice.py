
# * 1. Sum the Numbers. Create a list of numbers, print their sum.
# nums = [7,9,12,15,10,48,49,265]
# num2 = 0
# for i in nums:
#     num2 += i
# print(num2)

# * 2. Largest Number. Create a list of numbers, print the largest of the numbers.
# nums = [7,9,12,15,10,48,49,265]
# num1 = 0
# for x in nums:
#     if num1 < x:
#         num1 = x
# print(num1)

# * 3. Smallest Number. Create a list of numbers, print the smallest of the numbers.
# nums = [7, 9, 12, 15, 10, 48,3, 49, 265, -14 ]
# num1 = nums[0]
# for x in nums:
#     if x < num1:
#         num1 = x
# print(num1)

# * 4. Even Numbers. Create a list of numbers, print each number in the list that is even.
# nums = [7, 9, 12, 15, 10, 48,3, 49, 265]
# for x in nums:
#     if x % 2 == 0:
#         print(x)

# * 5. Positive Numbers. Create a list of numbers, print each number in the list that is greater than zero.
# nums = [7, 9, -4, -9, 12, 15, 10, 48,3, 49, 265]
# for x in nums:
#     if x > 0:
#         print(x)

# * 6. Positive Numbers II. Create a list of numbers, create a new list which contains every number in the given list which is positive.
# nums = [7, 9, -4, -9, 12, 15, 10, 48,3, 49, 265]
# num1 = []
# for x in nums:
#     if x > 0:
#         num1.append(x)
# print(num1)

# * 7. Multiply a list. Create a list of numbers, and a single factor(also a number), create a new list consisting of each of the numbers in the first list multiplied by the factor. Print this list.
# nums = [7, 9, -4, -9, 12, 15, 10, 48,3, 49, 265]
# num1 = [2]
# num2 = []
# for i in nums:
#     for j in num1:
#         num2.append(i*j)
# print(num2)

# * 8. Reverse a String. Given a string, print the string reversed.
# my_string = "hello"
# revstring = ""
# for i in my_string:
#     revstring = i + revstring
# print(revstring)

# * other solution
# string = "I am a little confused"
# i = 0
# new_string = ""
# while i< len(string):
#     new_string = string[i] + new_string
#     i+=1
# print(new_string)

# * 1. Multiply Vectors. Given two lists of numbers of the same length, create a new list by multiplying the pairs of numbers in corresponding positions in the two lists.
# list1 = [1, 3, 4, 6, 8]
# list2 = [4, 5, 6, 2, 10]
# list=[]
# for i, j in zip(list1, list2):
#     list.append(i*j)
# print(list)

# * 2. Matrix Addition. Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is represented as an list of lists:
# list1 = [[9,3],
#         [2,6]]
# list2 = [[8,2],
#         [4,0]]
# list3 = [[0,0],[0,0]]
# for i in range(len(list1)):
#     for j in range(len(list1[0])):
#         list3[i][j] = list1[i][j]+ list2[i][j]
# for x in list3:
#     print(x)
# ! have to practice with matrixes,

# ! did not know how to solve

# * 4. De-dup. Given a list of numbers or strings, create a new list containing the same elements as the first list, except with any duplicate values removed. Print the list.
# list1 = ["hello", "there", "hello", "there"]
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)

# * 5. Leetspeak. Given a paragraph of text as a String, print the paragraph in leetspeak(Links to an external site.).
# string1 ="I am a leet programmer"
# string = string1.upper()
# for i in string:
#     if i == "A":
#         string = string.replace('A','4')
#     elif i == "E":
#         string = string.replace('E', '3')
#     elif i == "G":
#         string = string.replace('G', '6')
#     elif i == "I":
#         string = string.replace('I', '1')
#     elif i == "O":
#         string = string.replace('O', '0')
#     elif i == "S":
#         string = string.replace('S', '5')
#     elif i == "T":
#         string = string.replace('T', '7')
# print(string)


# * 6. Long-long Vowels
# Given a word as a string, print the result of extending any long vowels to the length of 5.
# Examples:
# Good => Goooood
# Cheese => Cheeeeese
# Man => Man
# Spoon => Spooooon

# string1 = input("enter text")
# for i in (("a","a"*5),("e","e"*5),("i", "i"*5),("o", "o"*5), ("u", "u"*5)):
#     string1 = string1.replace(*i)
# print(string1)


# * 7. Caesar Cipher
# Given a string, print the Caesar Cipher ( or ROT13) of the string. What is Caesar Cipher? Learn about it here (Links to an external site.).
# Use your solution to decipher the following text: "lbh zhfg hayrnea jung lbh unir yrnearq"
#! found the solution online

# text1 = "lbh zhfg hayrnea jung lbh unir yrnearq"
# abc = "abcdefghijklmnopqrstuvwxyz"
# code1 = "".join([abc[(abc.find(c)+13) % 26] for c in text1])
# print(code1)
