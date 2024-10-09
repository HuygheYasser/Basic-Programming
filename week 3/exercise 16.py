import string
import random




# while assi[randy] != 'a':
#     randy = random.randint(0,len(string.ascii_letters)-1)


# print(assi[randy])


minimumlen=int(input("Give password minimum length: "))
maximumlen=int(input("Give password maximum length: "))


def generate_password_bis(minlen: int, maxlen: int):
    passw = ''
    randy = random.randint(minlen, maxlen)
    while randy != 0:
        randy2 = random.randint(0,len(string.ascii_letters)-1)
        assi = string.ascii_letters
        passw += assi[randy2]
        randy -= 1
    print(passw)



generate_password_bis(minimumlen, maximumlen)
