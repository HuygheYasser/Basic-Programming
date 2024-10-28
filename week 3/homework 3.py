# Ask the user for two years. Print the leap years between these two years. To do this, reuse the function 
# 'is_leap-year' which tests whether a year number is a leap year or not. 
# Enter the start year: 1993 
# Enter the end year: 2005 
# 1996 is a leap year 
# 2000 is a leap year 
# 2004 is a leap year


def is_leap_year(yearmax: int, yearmin: int):
    for i in range(sta, end):
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            print(f"{i} is leap year.")
        else:
            print(f"{i} is not a leap year")


sta = int(input("enter the start year: "))
end = int(input("enter the end year: "))



is_leap_year(sta, end)









