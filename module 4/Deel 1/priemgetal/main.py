from functions import is_prime

def get_prime_numbers(until:int) -> list:
  prime_numbers = []
  for number in range(until):
    if is_prime(number):
      prime_numbers.append(number)
  return prime_numbers


def get_prime_numbers_amount(until:int) -> int:
  prime_numbers = 0
  for number in range(until):
    if is_prime(number):
      prime_numbers += 1
  return prime_numbers

def get_prime_numbers_between_two_numbers(start:int, stop:int) -> list:
  prime_numbers = []
  for number in range(start, stop):
    if is_prime(number):
      prime_numbers.append(number)
  return prime_numbers

while True:
    keuze = input("Wat wil je doen?\n1: priemgetallen tot een getal,\n2: aantal priemgetallen tot een getal,\n3: priemgetallen tussen twee getallen,\n> ")
    if keuze in ["1", "2", "3"]: break
    print("Het moet alleen '1', '2' of '3' zijn.")

if keuze == "1":
    getal = int(input("Tot welk getal wil je de priemgetallen zien? "))
    getallen = get_prime_numbers(getal)
    if getallen: print(getallen)
    else: print("Er zijn geen priemgetallen tot", getal)

if keuze == "2":
    getal = int(input("Tot welk getal wil je het aantal priemgetallen zien? "))
    aantal = get_prime_numbers_amount(getal)
    print("Er zijn", aantal, "priemgetallen tot", getal)

if keuze == "3":
    getal1 = int(input("Wat is het eerste getal? "))
    getal2 = int(input("Wat is het tweede getal? "))
    getallen = get_prime_numbers_between_two_numbers(getal1, getal2)
    if getallen: print(getallen)
    else: print("Er zijn geen priemgetallen tussen", getal1, "en", getal2)