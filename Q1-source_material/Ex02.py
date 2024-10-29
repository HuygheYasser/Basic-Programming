# Ex02  *ssb   wawaawa 
# Huyghe Yasser MCTE MTS1

import random

def make_couples(unames:list[str],coupleamount: int) -> dict[str]:
    dictnames = {}
    if len(unames) < (coupleamount * 2):
        return "Not enough people for the amount of couples"
    else:
        while unames != [] and coupleamount != 0:
            try:
                a = random.choice(unames)
                unames.remove(a)
                b = random.choice(unames)
                unames.remove(b)
                dictnames.update({a:b})
                coupleamount -= 1
            except:
                return dictnames
    return dictnames





# test your function 
print("💘 The couples of  Howest are 💘")
students = ["Karel", "Ben", "Tim", "Ken", "Henk", "Lies", "Barbie", "Sandra", "Debbie"]
print(students)
number_couples = int(input("How many couples should be formed?:> "))
coupledict = make_couples(students,number_couples)
print(coupledict)
for key, value in coupledict.items():
    print(f"{key} 💘 {value}")


