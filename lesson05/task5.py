src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]

unique_list = set()

for el in src:
    if el not in unique_list:
        unique_list.add(el)
    else:
        unique_list.discard(el)

final_res = []
for el in src:
    if el in unique_list:
        final_res.append(el)

print(unique_list)
print(final_res)
print(result)
