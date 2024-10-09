import random

# randy = 0

# while randy != 1:
#     randy = random.randint(1, 20)
#     if randy == 1:
#         break


# print(randy)

randy = random.randint(1,20)
tries = 0

guess = int(input("guess a num between 1 and 20: "))

while guess != randy:
    if guess > randy:
        print("The number is too big")
        tries += 1
        guess = int(input("guess a num between 1 and 20: "))
    else:
        print("the number is too small")
        tries += 1
        guess = int(input("guess a num between 1 and 20: "))

print("Congratulations you guessed it :)")


