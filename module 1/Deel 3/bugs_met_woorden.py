woord1 = input("Voer woord 1 in: ")
woord2 = input("Voer woord 2 in: ")

if len(woord1) > len(woord2): print("Woord 1 heeft meer letters dan woord 2")
elif len(woord1) < len(woord2): print("Woord 2 heeft meer letters dan woord 1")
else: print("Woord 1 en woord 2 hebben even veel letters")