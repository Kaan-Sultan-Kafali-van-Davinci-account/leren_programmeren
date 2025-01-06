import random, time

rondes = 0
score = 0

while rondes <= 20:
    poging = 0
    getal = random.randrange(1, 1000)

    print(getal)

    while poging <= 10:
        while True:
            try:
                raad = int(input("Raad het getal van 1 tot 1000: "))
                break
            except:
                print("Dat was niet een getal...")
                time.sleep(0.5)

        if poging < 11:
            if raad == getal:
                print("Correct!")
                score += 1
                time.sleep(1.5)
                break

            elif raad > getal:
                print("Lager")
                time.sleep(0.5)

            elif raad < getal:
                print("Hoger")
                time.sleep(0.5)

            if abs(raad - getal) < 20:
                print("Heel warm")
            elif abs(raad - getal) < 50:
                print("Warm")

        poging += 1
        
        if poging == 8:
            print("3 pogingen...")
        if poging == 9:
            print("2 pogingen...")
        if poging == 10:
            print("Laatste poging...")
        if poging == 11:
            print("Verkeerd..."); time.sleep(1.5)

    print("Score:", score)

    while True:
        exit = input("Wil je nog een ronde? (j/n) ").lower()
        if exit in ["j", "n"]:
            break
        print("Dat verstond ik niet. Het moet alleen 'j' of 'n' zijn.")
    if exit == "n":
        break

print("- Game Over -")
print("Eindscore: ", score)