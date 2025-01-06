from name_and_age_functie import vraag

gegevens = vraag()

for gegeven in gegevens:
    print(gegeven["name"] + ", die in " + gegeven["place"] + " woont, is " + gegeven["age"] + " jaar")