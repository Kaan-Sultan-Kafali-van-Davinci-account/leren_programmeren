totaal = 0
som = [50]

while totaal < 1000:
    som.append(som[len(som) - 1] + 1)
    somstr = ""
    for no in som: somstr += f" + {no}"
    totaal = 0
    for no in som: totaal += no
    print(somstr[2:] + " =", totaal)