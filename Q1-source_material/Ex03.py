# Huyghe Yasser MCTE MTS1

import random

def select_random_gift(dict1:dict[str]) -> dict[str]:
    newdict = {}
    for key, value in dict1.items():
        newdict.update({key:random.choice(value)})
    return newdict


# test your function
dict_wishlists_persons = { "Stijn":["Bike", "Headphones", "Fitbit"], "Marie": ["Game", "Bike", "Screen", "Swimming band"], "Joerie": ["Racing bike", "Swimming band", "Book"], "Henk":["Laptop", "Beer Omer", "Bike"]}
print("Each person is randomly given a gift from their wish list.\nThis is the result:")
for key, value in select_random_gift(dict_wishlists_persons).items():
    print(f"{key} -> {value}")