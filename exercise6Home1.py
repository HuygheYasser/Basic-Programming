totalseconds = int(input("give the seconds: "))
totalminutes = totalseconds // 60
totalhours = totalminutes // 60

days = totalhours // 24

seconds = totalseconds%60
minutes = totalminutes%60
hours = totalhours%24



(f"d:h:m:s -> {days}:{hours}:{minutes}:{seconds}")






#eerst days, dan minutes, dan hours en dan seconds?
#86400 seconds in 1 day

#Just looking at it will not make it click. You have to look at each little step in detail and write some code using that concepts to see if it works how you understood it.
# toch beginnen met wat je weet (desondanks raad om te plannen) en zo puzzel vervolledigen
##soms eerst de equatie schrijven en erna een naam geven
# synthwave is good for focus, use glasses
#niet uit de flow geraken door jezelf iets (wss) nutteloos aan jezelf te willen bewijzen (zoals deze zin typen ook bvb lol)













# Sure! Let’s break down what each line does:

# seconds = total_seconds % 60:

# This line calculates the remaining seconds after converting the total seconds into minutes.
# The modulus operator % returns the remainder of the division of total_seconds by 60. This effectively gives you the number of seconds left over after you’ve counted full minutes.
# For example, if total_seconds is 125, then:

# 125 % 60 equals 5, so seconds would be 5.
# minutes = total_minutes % 60:

# Here, we find the remaining minutes after converting total minutes into hours.
# Again, the modulus operator is used to find the remainder when total_minutes is divided by 60. This gives you the minutes left over after you’ve counted full hours.
# Continuing the previous example, if total_minutes is 2 (which is derived from 125 seconds), then:

# 2 % 60 equals 2, so minutes would be 2.
# hours = total_hours % 24:

# This line calculates the remaining hours after converting total hours into days.
# The modulus operator here finds the remainder when total_hours is divided by 24, which tells you how many hours are left over after accounting for full days.
# If total_hours is 0 (from 125 seconds), then:

# 0 % 24 equals 0, so hours would be 0.
# In summary, these lines help extract the "leftover" seconds, minutes, and hours from the total input, allowing you to format the time accurately as days, hours, minutes, and seconds.