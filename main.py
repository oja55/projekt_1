"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Ondřej Vítek
email: ondra5510@gmail.com
discord: oja55#8858
"""

from task_template import TEXTS

users = {
    "bob": "123",
    "ann": "pas123",
    "mike": "password123",
    "liz": "pas123"
}

username = input("username: ")
password = input("password: ")
short_line = "-" * 40

if username not in users:
    print("Unregistered user, terminating the program..")

elif password == users.get(username):
    print(short_line,
          f"Welcome to the app, {username}\nWe have 3 texts to be analyzed.",
          short_line,
          sep="\n"
          )
    text_select = int(input("Enter a number btw. 1 and 3 to select: "))
    print(short_line)
    if 0 < text_select > 4:
        print("Wrong number, terminating the program..")
    else:
        words = TEXTS[text_select - 1]
        cleaned_words = []
        for word in words.split():
            cleaned_words.append(
                word.strip(",.")
            )
        titlecase = [x for x in cleaned_words if x.istitle()]
        uppercase = [x for x in cleaned_words if x.isupper() and x.isalpha()]
        lowercase = [x for x in cleaned_words if x.islower()]
        numeric = [x for x in cleaned_words if x.isnumeric()]
        print(f"There are {len(cleaned_words)} words in the selected text.",
              f"There are {len(titlecase)} titlecase words.",
              f"There are {len(uppercase)} uppercase words.",
              f"There are {len(lowercase)} lowercase words.",
              f"There are {len(numeric)} numeric strings.",
              f"The sum of all the numbers: {(sum(map(int, numeric)))}",
              short_line,
              sep="\n")
        print("LEN|", "OCCURENCES".center(17), "|NR")
        print(short_line)

        counted = {}
        quantity = []
        for letter in cleaned_words:
            counted[letter] = len(letter)
            if not counted.get(letter) in counted:
                quantity.append(len(letter))

        counts = {}
        for number in quantity:
            if number not in counts:
                counts[number] = 1
            else:
                counts[number] = counts[number] + 1

        for key, value in sorted(counts.items()):
            print(f"{key:3}| {('*' * value):17} |{value}")