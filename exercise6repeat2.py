total_seconds = int(input("give me the amount of seconds: "))

total_minutes = total_seconds//60
total_hours = total_minutes//60

seconds = total_seconds%60
minutes = total_minutes%60
hours = total_hours%24

days = total_hours // 24




print(f"d:h:m:s -> {days}:{hours}:{minutes}:{seconds}")