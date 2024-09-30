gastheer = True
gasten = True
drinken = True
eten = True

start_condition_1 = gastheer or gasten
start_condition_2 = gastheer or (gasten and eten and drinken)
start_condition_3 = not (eten and not drinken)
start_condition_4 = not (gasten and not (eten and drinken))
start_condition_5 = not (gastheer and not drinken)
start_condition_6 = not (eten and not drinken and not gastheer and not gasten)

if (start_condition_1 and start_condition_2 and start_condition_3 and start_condition_4 and start_condition_5 and start_condition_6): print('Start the Movie')
else: print('No Movie')