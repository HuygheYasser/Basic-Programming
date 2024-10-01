from calendar import month

totalmonths = ("january","february","march","april","may","june","july","august","september","october","november","december")

while True:
    year = input("give year: ")
    try:
        ayear = int(year)
        print("thanks!")
        break
    except ValueError:
        print("try again, not a year..")



while True:
    montho = input("give month: ").lower()
    if montho in totalmonths:
        amonth = totalmonths.index(montho)+1
        print("thanks")
        break
    else:
        print("spelling incorrect, try again")



print(month(ayear,amonth))