total_small = int(input("Hoeveel pizza small wil je bestellen? "))
total_medium = int(input("Hoeveel pizza medium wil je bestellen? "))
total_large = int(input("Hoeveel pizza large wil je bestellen? "))

pizza_small = 6.50
pizza_medium = 9.30
pizza_large = 11.10

small_total = pizza_small * total_small
medium_total = pizza_medium * total_medium
large_total = pizza_large * total_large

print("---------------- Bon -----------------")
print("Small Prijs: €" + str(small_total))
print("Medium Prijs: €" + str(medium_total))
print("Large Prijs: €" + str(large_total))
print("--------------------------------------")