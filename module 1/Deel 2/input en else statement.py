a = int(input("Eerste getal a "))
b = int(input("Tweede getal b "))

if a > b: max_ = a; print(f"a is het grootste getal: {max_}"); min_ = b
elif a < b: min_ = a; print(f"a is het kleinste getal: {min_}"); max_ = b
else: print("a en b staan even groot"); max_ = b; min_ = a