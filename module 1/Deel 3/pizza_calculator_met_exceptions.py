total_small = 0
total_medium = 0
total_large = 0

while True:
    input_small = input("Hoeveel pizza small wil je bestellen? ")
    try:
        total_small = int(input_small)
        if total_small >= 0: break
        else: print("Het moet een positieve getal zijn. Voer small opnieuw in.")
    except: print("Het moet een getal zijn. Voer small opnieuw in.")
while True:
    input_medium = input("Hoeveel pizza medium wil je bestellen? ")
    try:
        total_medium = int(input_medium)
        if total_medium >= 0: break
        else: print("Het moet een positieve getal zijn. Voer medium opnieuw in.")
    except: print("Het moet een getal zijn. Voer medium opnieuw in.")
while True:
    input_large = input("Hoeveel pizza large wil je bestellen? ")
    try:
        total_large = int(input_large)
        if total_large >= 0: break
        else: print("Het moet een positieve getal zijn. Voer large opnieuw in.")
    except: print("Het moet een getal zijn. Voer large opnieuw in.")

if total_small < 0: total_small = 0; print("Total small was negatief dus het beschouwd als 0")
if total_medium < 0: total_medium = 0; print("Total small was negatief dus het beschouwd als 0")
if total_large < 0: total_large = 0; print("Total small was negatief dus het beschouwd als 0")

pizza_small = 6.50
pizza_medium = 9.30
pizza_large = 11.10

small_total = pizza_small * total_small
medium_total = pizza_medium * total_medium
large_total = pizza_large * total_large

print("---------------- Bon -----------------")
if total_small: print("Small Prijs: €" + str(round(small_total, 2)))
if total_medium: print("Medium Prijs: €" + str(round(medium_total, 2)))
if total_large: print("Large Prijs: €" + str(round(large_total, 2)))
print("\nTotal Prijs: €" + str(round(small_total + medium_total + large_total, 2)))
print("--------------------------------------")