
import json


with open('phone_book.json', 'r') as fh:
    phone_book = json.load(fh)


# phone_book = {}
something = True

while something:

    choice = int(input("""
Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
What do you want to do (1-5)?
"""))

    if choice == 1:
        search = str(input('Name: '))
        if search in phone_book:
            print(f'{search}: {phone_book[search]}')
        elif search not in phone_book:
            print(f'{search} is not an entry')

    elif choice == 2:
        name1 = str(input("Name: "))
        number1 = str(input("Number: "))
        phone_book[name1] = number1
        print(f" {name1} was saved.")

    elif choice == 3:
        search = str(input('Name: '))
        if search in phone_book:
            del phone_book[search]
            print(f' {search} deleted')

    elif choice == 4:
        for x in phone_book:
            print(f'{x}: {phone_book[x]}')

    elif choice == 5:
        with open('phone_book.json', 'w') as fh:
            json.dump(phone_book, fh)
        break

print('Bye.')
