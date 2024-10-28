# Ask the user for a word. Loop over each character in the word and delete all vowels. 
# Enter a word: apple tree 
# The string with the deleted vowels is: *ppl* tr** 


word = input("Give a word: ")

vowels = ('aeiou')

for e in word:
    if e in vowels:
        word = word[:word.index(e)] + word[word.index(e)+1:]

print(word)
















# vowels = ('aeiou')
# cons = 0

# word = input("give word: ")

# for e in word:
#     if not e in vowels:
#         cons += 1

# print(cons)

# little test above

