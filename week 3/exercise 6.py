a = int(input("give first number (start value): "))
b = int(input("give second number (stop value value): "))


print(f"the numbers you are looking for between {a} and {b} are:")

for i in range(a, b+1):
    if i % 7 == 0 and i % 5 != 0:
        print(i)