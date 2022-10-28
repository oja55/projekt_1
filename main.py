"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Ondřej Vítek
email: ondra5510@gmail.com
discord: oja55#8858
"""


from task_template import TEXTS

users = {
    "bob" : "123",
    "ann" : "pas123",
    "mike" : "password123",
    "liz" : "pas123"
}

username = input("username: ")
password = input("password: ")
carky = "-" * 40

if not username in users:
    print("Unregistered user, terminating the program..")

elif password == users.get(username):
    print(carky,
          f"Welcome to the app, {username}\nWe have 3 texts to be analyzed.",
          carky,
          sep="\n"
    )
    text_select = int(input("Enter a number btw. 1 and 3 to select: "))
    print(carky)
    if 0 < text_select > 4:
        print("Wrong number, terminating the program..")
    else:

        words = TEXTS[text_select - 1]
        vycistena_slova = list()
        for slovo in words.split():
            vycistena_slova.append(
                slovo.strip(",.")
                )
        titlecase = [x for x in vycistena_slova if x.istitle()]
        uppercase = [x for x in vycistena_slova if x.isupper()]
        lowercase = [x for x in vycistena_slova if x.islower()]
        numeric = [x for x in vycistena_slova if x.isnumeric()]
        print(f"There are {len(vycistena_slova)} words in the selected text.",
              f"There are {len(titlecase)} titlecase words.",
              f"There are {len(uppercase)} uppercase words.",
              f"There are {len(lowercase)} lowercase words.",
              f"There are {len(numeric)} numeric strings.",
              f"The sum of all the numbers: {(sum(map(int, numeric)))}",
              carky,
              sep="\n")

        print("LEN|", "OCCURENCES".center(15), "|NR")
        print(carky)


        counted = {}
        for letter in vycistena_slova:
            counted[letter] = len(letter)

        pocet = list(counted.values())

        counts = {}
        for number in pocet:
            if not number in counts:
                counts[number] = 1
            else:
                counts[number] = counts[number] + 1

        for key, value in sorted(counts.items()):
            print(f"{key:3}| {('*' * value):15} |{value}")



