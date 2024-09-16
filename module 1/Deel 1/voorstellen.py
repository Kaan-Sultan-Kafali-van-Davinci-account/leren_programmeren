naam = input("Wat is je naam? ")
leeftijd = int(input("Hoe oud ben je? "))
geslacht = input("Ben je een A) een jonge of B) een meisje? ").lower()
fevoriete_kleur = input("Wat is je favoriete kleur? ")
favoriete_getal = int(input("Wat is je favoriete getal? "))
leeftijdsverschil = abs(leeftijd-favoriete_getal)
geslachts_term = 'haar' if geslacht == 'b' else 'zijn'

print("")
print("Mag ik je voorstellen aan", naam)
print(f"{geslacht.capitalize()} leeftijd is:", leeftijd)
print(f"{naam}'s favoriete kleur is:", fevoriete_kleur)
print(f"Het verschil tussen {leeftijd} leeftijd en {favoriete_getal} is:", leeftijdsverschil)
