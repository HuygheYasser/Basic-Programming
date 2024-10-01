cels = float(input("Give temp in Celsius: "))

fahr = round(((cels * 9/5) + 32), 1)
kelv = round((cels + 273.15), 1)

print(f" fahrenheit:{fahr}, kelvin:{kelv}")
# use python round for 2 decimals