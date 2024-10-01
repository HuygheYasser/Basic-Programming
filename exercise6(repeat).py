seconds = int(input("enter the number of seconds: "))

days = seconds//24//60//60
hours = (seconds%24%60%60)

print(f"d:h:m:s -> {seconds//24//60//60}:{seconds%24%60%60//60//60}:{seconds%24%60%60%60%60//60}:{seconds}")

# print(f"d:h:m:s -> {seconds//24//60//60}:{seconds//60//60}:{seconds//60}:{seconds}")


#  control K+C  to comment everything,   control  K+U to uncomment
#  9 // 2 = 4  (floor division)      BUT    9 % 2 = 1    (modulo)     ZIJN GEWONE SLASHES, GEEN BACKSLASH





