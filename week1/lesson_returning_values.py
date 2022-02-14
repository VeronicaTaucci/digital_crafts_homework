
# ! https://digitalcrafts.instructure.com/courses/189/pages/lesson-returning-values?module_item_id=23009

# * Madlib
# Write a function that asks a user for a noun, a present-tense verb, and a name. Print a story that uses these words to the console.
# Example output:
# There once was a[NOUN] that suddenly came to life, called themselves[NAME] and starting[VERB] around the town. [NAME] decided that[VERB] was unacceptable and decided to move to the countryside an live a life of solitude.

# name = input("What is your name?")
# noun = input("What is the noun?")
# verb = input("What is the verb?(present-tense) ")
# print(f"There once was a {noun} that suddenly came to life, called themselves {name} and starting {verb} around the town. {name}decided that {verb} was unacceptable and decided to move to the countryside an live a life of solitude.")

# * Tip Calculator: Write a function called percentagePlus that takes a bill total and a tip percentage and returns(not prints) the total plus tip. Create a second function called tipCalculator that asks the user for the bill total and the tip percentage. Pass those values through to the tipCalculator function and then print the result in a nice format.
bill_total = float(input("What is the total bill?"))
tip_percent = int(input("What is the tip percent?"))
number_ppl = int(input("How many people?"))
tip_amount = (100 * tip_percent) / bill_total
payment_each = (
    round(float(((tip_percent / 100 + 1) * bill_total) / number_ppl), 2))
print(f"Your total bill is: $ {bill_total}")
print(f"each person owes: $ {payment_each}")
