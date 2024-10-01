from math import pi

# rad = float(input("give radiant length: "))

# surface = round((pi * rad ** 2),2)

# print(f"the surface of the circle with radiance {rad} equals {surface}")

# # use from to not have to import the entire library







# rad=float(input("give radiant length in cm: "))

# volume = 4/3* pi * (rad**3)

# print(f"sphere with radiant {rad} has a volume of {volume} cm³")










# import calendar


# year = int(input("Enter year: "))

# month = input("enter month: ")

# totalmonths = ("january","february","march","april","may","june","july","august","september","october","november","december")


# for t in totalmonths:
#     if month.lower() == t:
#         actualmonth= totalmonths.index(t) + 1


# #print(actualmonth)

# print(calendar.month(year, actualmonth))



from multiprocessing import cpu_count

print(cpu_count())

