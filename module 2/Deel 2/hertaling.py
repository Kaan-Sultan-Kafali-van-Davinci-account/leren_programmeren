tekst = input("Voer tekst in: ")
h = {
    "kat": "kreeft",
    "ja": "nee",
    "zon": "maan",
    "jaar": "seconde",
    "boos": "heel erg rustig",
    }

#for woord in h:
    #tekst = tekst.replace(woord, h[woord])

woorden = tekst.split(" ")
zin = ""
for woord in woorden:
    if woord in h: zin += h[woord] + " "
    else:  zin += woord + " "

print(zin)