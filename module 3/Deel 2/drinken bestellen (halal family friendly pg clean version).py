PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

VIP_LIST = ('jeroen', 'jouke', 'rudi')

#bouw hieronder de floowchart na

age = int(input("Hoe oud ben jij? "))
sticker = False
band = ""

if age >= 18:
    name = input("Wat is jouw naam? ")
    vip = name in VIP_LIST
    if vip:
        if age >= 21:
            band = "blauw"
            print("Je krijgt een blauwe kleur band.")
        else:
            band = "rood"
            print("Je krijgt een rode kleur band.")
    else:
        if age >= 21:
            sticker = True
            print("Je krijgt een sticker")
            
    drink = input("Wat wil je drinken? (water, aardbeienmelk, appelsap) ")

    
    if drink == "water":
        if band:
            print("Hier is jouw water, complimenten van het huis")
        else:
            print("Water, dat is dan €0,50")

    elif drink == "aardbeienmelk":
        if band or sticker:
            if band:
                print("Hier is jouw aardbeienmelk, complimenten van het huis")
            else:
                print("Aardbeienmelk, dat is dan €1,25")
        else:
            print("Sorry, je mag geen aardbeienmelk bestellen onder de 21!")

    elif drink == "appelsap":
        if band:
            if band == "blauw":
                print("Appelsap, dat is dan €1,00")
            else:
                print("Sorry, je mag geen appelsap bestellen onder de 21!")
        else:
            print("Sorry, alleen de vips mogen dat!")
    
    else:
        print("Dat hebben we niet. Hier is toch jouw water: 🌊")

else:
    print("Sorry je mag er niet binnen!")