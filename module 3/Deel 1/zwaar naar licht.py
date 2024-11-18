import fruitmand

for fruit in sorted(fruitmand.fruitmand, key=lambda x: x["weight"], reverse=True):
    print(fruit["name"], fruit["weight"])