from functions import *

def calculate(n1, n2):
    if choice == "a":
        answer = add(n1, n2)

    elif choice == "b":
        answer = subtract(n1, n2)

    elif choice == "c":
        answer = multiply(n1, n2)

    elif choice == "d":
        answer = divide(n1, n2)

    elif choice == "e":
        answer = increase(n1)

    elif choice == "f":
        answer = decrease(n1)

    elif choice == "g":
        answer = double(n1)

    elif choice == "h":
        answer = half(n1)

    return answer



while True:
    choice = input("Wat wilt u doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren? ").lower()
    if choice in ["a", "b", "c", "d", "e", "f", "g", "h"]: break
    else: print("Dat was niet één van de keuze")

if choice in ["a", "b", "c", "d"]:
    n1 = float(input("Geef het eerste getal: "))
    n2 = float(input("Geef het tweede getal: "))

elif choice in ["e", "f", "g", "h"]:
    n1 = float(input("Geef het getal: "))
    n2 = 0

answer = calculate(n1, n2)

while True:
    print(f"Antwoord: " + str(answer))
    while True:
        choice_remember = choice
        choice = input("Wil je nog iets met dit getal " + str(answer) + " doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen, H) getal halveren? of I) niets? ").lower()
        if choice in ["a", "b", "c", "d", "e", "f", "g", "h", "i", ""]: break
        else: print("Dat was niet één van de keuze")

    if choice in ["a", "b", "c", "d"]:
        n2 = float(input("Geef het getal: "))
    
    if choice == "i":
        break

    answer = calculate(answer, n2)

    if choice == "":
        answer = calculate(answer, n2)