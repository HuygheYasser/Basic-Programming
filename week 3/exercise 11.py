def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")



starty=int(input("Give the start year: "))
endy=int(input("Give the end year: "))


for i in range(starty, endy + 1):
    is_leap_year(i)