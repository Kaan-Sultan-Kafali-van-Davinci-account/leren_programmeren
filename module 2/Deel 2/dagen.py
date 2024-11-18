dagen = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")

print("Alle dagen van de week zijn:")
for dag in dagen: print("- " + dag)

string = "\nDe weekenddagen zijn:"
i = 3
for index, dag in enumerate(dagen[-i:]):
    string += " " + dag
    if index == 2: string += "."
    else: string += " &"
print(string)

string = "\nDe werkdagen zijn:"
for index, dag in enumerate(dagen[:-2]):
    string += " " + dag
    if index == 4: string += "."
    elif index == 3: string += " &"
    else: string += ","
print(string)

dagen = list(dagen)
dagen.reverse()
dagen = tuple(dagen)

string = "\nAlle dagen van de week in omgekeerde volgorde zijn:"
for index, dag in enumerate(dagen):
    string += " " + dag
    if index == 6: string += "."
    else: string += " ->"
print(string)

print("\nDe werkdagen in omgekeerde volgorde zijn:")
for dag in dagen[-5:]: print("- " + dag)

string = "\nDe weekenddagen in omgekeerde volgorde zijn:"
for index, dag in enumerate(dagen[:-5]):
    string += " " + dag
    if index == 0: string += " +"
print(string)