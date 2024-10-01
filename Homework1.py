land = float(input("give landprice: "))
building = float(input("give buildingprice: "))

vat = (land + building) / 100 * 21

total = land + building + vat


print("total cost of the project is: ", total)