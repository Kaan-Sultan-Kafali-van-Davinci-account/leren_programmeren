from functions import *

def calculate(n1, n2):
    global answer
    if choice == "a":
        answer = CALCULATIONS["add"](n1, n2)

    if choice == "b":
        answer = CALCULATIONS["subtract"](n1, n2)

    if choice == "c":
        answer = CALCULATIONS["multiply"](n1, n2)

    if choice == "d":
        answer = CALCULATIONS["divide"](n1, n2)

    if choice == "e":
        answer = CALCULATIONS["increase"](n1)

    if choice == "f":
        answer = CALCULATIONS["decrease"](n1)

    if choice == "g":
        answer = CALCULATIONS["double"](n1)

    if choice == "h":
        answer = CALCULATIONS["half"](n1)

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

    answer = calculate(answer, n2)

    if choice == "i": break

    if choice == "":
        answer = calculate(answer, n2)