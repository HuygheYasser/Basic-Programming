# Ex01

# Huyghe Yasser MCTE MTS1

def calculate_love_score(name1:str,name2:str) -> int:
    uniqletters = []
    name1=name1.lower()
    name2=name2.lower()
    for i in name1:
        if i in name2 and i not in uniqletters:
            uniqletters.append(i)
    countuniq = len(uniqletters)
    averlen = (len(name1) + len(name2)) /2
    perce = countuniq / averlen
    return f"{int(perce * 100)}%"

first_name = input("Enter a first name:> ")
second_name = input("Enter a second name:> ")

print(calculate_love_score(first_name,second_name))




# test your function 
first_name = input("Enter a first name:> ")
second_name = input("Enter a second name:> ")
# print(f"The love score between {first_name} and {second_name} is {calculate_love_score(first_name, second_name)}")


