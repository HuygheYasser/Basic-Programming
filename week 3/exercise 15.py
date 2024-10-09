howest = input("Give howest mail adress: ")



for e in howest:
    if e == '.':
        middex = howest.index(e)

for a in howest:
    if a == '@':
        enddex = howest.index(a)





print(f"The last name is {howest[middex+1:enddex]} and the first name is {howest[:middex]}")