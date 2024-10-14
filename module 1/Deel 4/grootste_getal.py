def vergelijk_en_return_grootste(n1, n2):
    if n1 == n2: return "Beide getallen zijn even groot"
    elif n1 > n2: return f"Maximum: {n1} en minimum: {n2}"
    elif n1 < n2: return f"Maximum: {n2} en minimum: {n1}"