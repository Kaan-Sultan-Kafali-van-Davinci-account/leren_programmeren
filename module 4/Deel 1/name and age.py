def ask():
    name = input("Wat is jouw naam? ")
    age = input("Hoe oud ben jij? ")
    return {"name": name, "age": age}

gegevens = ask()

print(gegevens["name"] + " is " + gegevens["age"] + " jaar oud")