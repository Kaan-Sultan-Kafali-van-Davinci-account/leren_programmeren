from studieadviestext import *

print(STUDIEDOKTER_TITEL)
weken = int(input(AANTAL_WEKEN_VRAAG))
print(COMPETENTIE_STELLING_1)
score1 = int(input(OPTIES))
print(COMPETENTIE_STELLING_2)
score2 = int(input(OPTIES))
print(COMPETENTIE_STELLING_3)
score3 = int(input(OPTIES))
print(COMPETENTIE_STELLING_4)
score4 = int(input(OPTIES))
print(COMPETENTIE_STELLING_5)
score5 = int(input(OPTIES))
if weken >= 10:
  print(COMPETENTIE_STELLING_6)
  score6 = int(input(OPTIES))
  print(COMPETENTIE_STELLING_7)
  score7 = int(input(OPTIES))
score = (score1 + score2 + score3 + score4 + score5 + score6 + score7) / 7
print(COMPETENTIE_ADVIES_TITEL)

if score <= 3: print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
elif score <= 2: print(COMPETENTIE_ADVIES_ZORGELIJK)
else: print(COMPETENTIE_ADVIES_GERUSTSTELLEND)