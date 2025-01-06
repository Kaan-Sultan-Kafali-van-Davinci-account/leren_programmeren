def ask():
    name = input("Wat is jouw naam? ")
    place = input("Waar woon jij? ")
    age = input("Hoe oud ben jij? ")
    return {"name": name, "place": place, "age": age}

def vraag():
    verzameling = []
    stop_of_enter = "enter"
    while stop_of_enter == "enter":
        verzameling.append(ask())
        stop_of_enter = input("Toets \"enter\" om door te gaan of \"stop\" om te printen: ")
        while True:
            if stop_of_enter == "stop":
                break
            elif stop_of_enter == "enter":
                break
            else:
                stop_of_enter = input("Toets \"enter\" om door te gaan of \"stop\" om te printen: ")
    return verzameling

gegevens = vraag()

for gegeven in gegevens:
    print(gegeven["name"] + ", die in " + gegeven["place"] + " woont, is " + gegeven["age"] + " jaar")