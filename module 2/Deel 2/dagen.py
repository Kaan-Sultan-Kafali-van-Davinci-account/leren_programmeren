dagen = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")

print("Alle dagen van de week zijn:")
for dag in dagen: print("- " + dag)

string = "\nDe weekenddagen zijn:"
for dag in dagen[-2:]: string += " " + dag
print(string)

string = "\nDe werkdagen zijn:"
for dag in dagen[:-2]: string += " " + dag
print(string)

dagen = list(dagen)
dagen.reverse()
dagen = tuple(dagen)

string = "\nAlle dagen van de week in omgekeerde volgorde zijn:"
for dag in dagen: string += " " + dag
print(string)

print("\nDe werkdagen in omgekeerde volgorde zijn:")
for dag in dagen[-5:]: print("- " + dag)

string = "\nDe weekenddagen in omgekeerde volgorde zijn:"
for dag in dagen[:-5]: string += " " + dag
print(string)