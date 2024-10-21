aantal = int(input("Hoeveel lijsten? "))
lists = []
for i in range(aantal):
    current_len = int(input("Hoe lang moet lijst " + str(i + 1) + " zijn "))
    current_list = []
    for j in range(current_len): current_list.append((j + 1) * (i + 1))
    lists.append(current_list)
print(lists)