# Ask the user for a word. Run over each character in the word, counting the number of vowels and 
# consonants. Afterwards, print both numbers. 
# Enter a word: apple 
# Number of vowels: 2 
# Number of consonants: 3 

vow = ['a','e','i','o','u']

numvow = 0
numcon = 0

word = input("give word: ")

for i in word:
    if i in vow:
        numvow += 1
    else:
        numcon+=1


print(f"vowels:{numvow}, consonants: {numcon}")

    

