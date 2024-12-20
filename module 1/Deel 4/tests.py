#import hier je functie "from [bestandsnaamZonderExtentie] import [functieNaam]"
from grootste_getal import vergelijk_en_return_grootste
from test_lib import test, report

expected = "Beide getallen zijn even groot" #resultaat
result = vergelijk_en_return_grootste(6002, 6002) #roep hier je functie aan met 2 dezelfde getallen
test('TEST nr1=nr2', expected, result)

expected = "Maximum: 2091 en minimum: 327" #resultaat
result = vergelijk_en_return_grootste(2091, 327) #roep hier je functie aan waar nr1 groter is dan nr2
test('TEST nr1>nr2', expected, result)

expected = "Maximum: 95847 en minimum: 13" #resultaat
result = vergelijk_en_return_grootste(13, 95847) #roep hier je functie aan  waar nr1 kleiner is dan nr2
test('TEST nr1<nr2', expected, result)

if __name__ == "__main__": report()