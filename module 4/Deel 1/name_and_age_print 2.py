from name_and_age_functie import vraag
from termcolor import colored as c

gegevens = vraag()

for gegeven in gegevens:
    if int(gegeven["age"]) < 18: volwassen = "nog niet"
    else: volwassen = "al " + str(int(gegeven["age"]) - 18) + " jaar"
    print("In " + c(gegeven["place"], "yellow") + " woont " + c(gegeven["name"], "green") + ", die " + c(volwassen, "red") + " volwassen is")