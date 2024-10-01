days=float(input("Enter the number of days:"))
hours=float(input("Enter the number of hours:"))
minutes=float(input("Enter the number of minutes:"))
seconds=float(input("Enter the number of seconds:"))

print(f"the total amount of seconds is {seconds + (minutes*60) + (hours * 60 * 60) + (days * 24 * 60 * 60)}")