def ask():
    name = input("Wat is jouw naam? ")
    place = input("Waar woon jij? ")
    while True:
        try:
            age = int(input("Hoe oud ben jij? "))
            break
        except:
            print("Dat was geen getal!")
    age = str(age)
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