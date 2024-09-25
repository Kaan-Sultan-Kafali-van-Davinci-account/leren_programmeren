gastheer = True
gasten = True
drinken = True
eten = True

#Een feest moet minimaal gasten of een gastheer hebben.
start_condition_1 = gastheer or gasten
start_condition_2 = gastheer or (gasten and drinken and eten)
start_condition_3 = eten and not drinken
start_condition_4 = eten and drinken
start_condition_5 = gastheer and drinken
start_condition_6 = not (eten and not drinken and not gastheer and not gasten)

voorwaarden = {
"[True, True, True, True]": True,
"[False, True, True, True]": True,
"[True, False, True, True]": True,
"[True, True, False, True]": True,
"[True, True, True, False]": False,
"[False, False, True, True]": False,
"[False, False, False, True]": False,
"[False, False, False, False]": False,
"[True, True, False, False]": False,
"[True, True, False, True]": True,
"[True, False, False, True]": True,
"[True, False, True, False]": False,
"[False, True, True, False]": False,
"[False, True, False, True]": True,
"[True, False, False, False]": False,
"[False, True, False, False]": False,
"[False, False, True, False]": False,
"[False, False, False, True]": False,
}

eind_voorwaard = start_condition_1 or start_condition_2 or start_condition_3 or start_condition_4 or start_condition_5 or start_condition_6

if voorwaarden[str([gastheer, gasten, eten, drinken])]: print('Start the Movie')
else: print('No Movie')