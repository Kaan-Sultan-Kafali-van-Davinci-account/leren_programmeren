#import hier je functie "from [bestandsnaamZonderExtentie] import [functieNaam]"
from grootste_getal import vergelijk_en_return_grootste
from test_lib import test, report

expected = '' #resultaat
result = vergelijk_en_return_grootste(6002, 6002) #roep hier je functie aan met 2 dezelfde getallen
test('TEST nr1=nr2', expected, result)

expected = '' #resultaat
result = vergelijk_en_return_grootste(2091, 327) #roep hier je functie aan waar nr1 groter is dan nr2
test('TEST nr1>nr2', expected, result)

expected = '' #resultaat
result = vergelijk_en_return_grootste(13, 95847) #roep hier je functie aan  waar nr1 kleiner is dan nr2
test('TEST nr1<nr2', expected, result)

if __name__ == "__main__":
    report()

#er is een bug waar het een lege string verwacht??