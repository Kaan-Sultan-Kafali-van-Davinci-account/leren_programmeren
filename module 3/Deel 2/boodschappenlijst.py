producten = {}
exit = False

while not exit:
    p = input("Wat zou je willen bestellen? ").lower()
    try:
        if not p in producten:
            producten[p] = int(input("Hoeveel zou je van " + p + " willen? "))
        else:
            producten[p] += int(input("Hoeveel zou je van " + p + " willen toevoegen? "))
    except:
        print("Dat was geen getal! Probeer artikel weer toe te voegen")
    while True:
        exit_input = input("Wil je nog verder? (j/n) ").lower()
        if exit_input in ["j", "n"]:
            exit = exit_input == "n"
            break
        else:
            print("Dat verstond ik niet. Het moet alleen 'j' of 'n' zijn.")

print("--[ BOODSCHAPPENLIJST ]--\n")
for p in producten: print(str(producten[p]) + "x", p)
print("\n-------------------------")