toegang = 7.45

personen = 4

cent_vr = 0.37

vijf_minuten = 9

prijs = (personen * toegang) + ((vijf_minuten * cent_vr) * personen)

print(f"Dit geweldige dagje-uit met {personen} mensen in de Speelhal met {vijf_minuten * 5} minuten VR kost je maar {round(prijs, 2)} euro")
