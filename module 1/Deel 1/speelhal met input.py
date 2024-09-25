toegang = float(input("Hoeveel zal de toegang moeten kosten? ")) #(default €7,45)

personen = int(input("Hoeveel mensen zijn er? "))

cent_vr = float(input("Hoeveel zal de VR moeten kosten? ")) #(default €0,37)

vijf_minuten = int(input("Voor hoeveel minuten willen jullie op de VR spelen? ")) / 5

#prijs = (personen * toegang) + ((vijf_minuten * cent_vr) * personen)
prijs = (toegang + (vijf_minuten * cent_vr)) * personen
print(f"Dit geweldige dagje-uit met {personen} mensen in de Speelhal met {vijf_minuten * 5} minuten VR kost je maar {round(prijs, 2)} euro")
