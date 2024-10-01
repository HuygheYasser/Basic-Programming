from calendar import month


year = int(input("give year: "))


totalmonths = ("january","february","march","april","may","june","july","august","september","october","november","december")






while True:
    month_input = input("Give month: ").lower()  # Read input and convert to lowercase

    if month_input in totalmonths:  # Check if the month is valid
        actualmonth = totalmonths.index(month_input) + 1  # Get the month number  # Print the calendar
        break  # Exit the loop if everything is fine
    else:
        print("Invalid month. Please try again.")


print(month(year, actualmonth))


# for t in totalmonths:
#     if t == monthy.lower():
#         actualmonth = totalmonths.index(t) + 1
#     else:
#         print("month is invalid, please try again")
#         break

# print(month(year, actualmonth))
