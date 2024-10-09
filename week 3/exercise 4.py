collection = []

for i in range(11,130,2):
    collection.append(i)

strcol = ', '.join(map(str, collection))

print(strcol)