gastheer = input("Wie is the gastheer? ").capitalize()
gasten = 6
drinken = True
eten = True

#Een feest moet minimaal gasten of een gastheer hebben.
start_condition_1 = gastheer or gasten
start_condition_2 = gastheer or (gasten and drinken and eten)
start_condition_3 = drinken or not eten
start_condition_4 = eten and drinken
start_condition_5 = gastheer or drinken
start_condition_6 = not (eten and not drinken and not gastheer and not gasten)
start_condition_7 = not gastheer == "Eugéne"
start_condition_8 = gastheer == "Kaan"
start_condition_9 = gasten >= 4
start_condition_10 = gasten <= 20

if ((start_condition_1 and start_condition_2 and start_condition_3 and start_condition_4 and start_condition_5 and start_condition_6 and start_condition_7) or start_condition_8) and start_condition_9 and start_condition_10:
    print('Start the Movie')
else:
    print('No Movie')