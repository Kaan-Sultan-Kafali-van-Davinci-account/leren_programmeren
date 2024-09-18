gastheer = True
gasten = True
drinken = True
eten = True

#Een feest moet minimaal gasten of een gastheer hebben.
start_condition_1 = gastheer or gasten
start_condition_2 = gastheer or (gasten and drinken and eten)
start_condition_3 = drinken or not eten
start_condition_4 = eten and drinken
start_condition_5 = gastheer and drinken
start_condition_6 = not (eten and not drinken and not gastheer and not gasten)

if start_condition_1 and start_condition_2 and start_condition_3 and start_condition_4 and start_condition_5 and start_condition_6:
    print('Start the Movie')
else:
    print('No Movie')
