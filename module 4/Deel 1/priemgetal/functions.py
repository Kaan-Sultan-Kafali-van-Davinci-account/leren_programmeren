# Controleert of een getal een priemgetal is.
def is_prime(number:int) -> bool:
    # Als de getal lager dan 1 is
    if number <= 1:
        return False
    
    # Als de getal 2 is
    if number == 2:
        return True
    
    # Als de getal even in
    if number % 2 == 0:
        return False
    
    # Kijkt of de getal deelbaar is door een oneven getal
    max_divisor = int(number**0.5) + 1
    for d in range(3, max_divisor, 2):
        if number % d == 0:
            return False
    
    # Return true als het getal een priemgetal is
    return True