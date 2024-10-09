# At the end, print out the total cost for each category, as well as the average price for each category. We 
# use the function 'give_ticket_by_category' for this purpose. 


# Specify the number of products you wish to enter:> 5 
# What is the category? [V: Vegetable, F: Fruit, B: Beverage]> B 
# What is the cost price of the product:> 10 

# 2 products are in the category Vegetables 
# Total cost: 21.3 
# Average price per product: 10.65 

# 1 products are in the category Fruit 
# Total cost price: 4.0 
# Average price per product: 4.00 

def give_ticket_by_category(categname: str, sumprice: float, categnum: int):
    if categnum != 0:
        print(f"\n{categnum} products are in the category {categname}")
        print(f"Total cost: {round(sumprice, 2)}")
        print(f"Average price per product: {round(sumprice/categnum,2)}")


vegetables = 0
fruit = 0
beverage = 0

costveg = 0
costfruit = 0
costbever = 0


prodamount = int(input("Specify the number of products you wish to enter: "))

while prodamount != 0:
    category = input("What is the category [V: Vegetable, F: Fruit, B: Beverage]: ")
    if category.upper() == 'V':
        vegetables+=1
        prodamount-=1
        costveg += float(input("What is the cost of the product? "))
    elif category.upper() == 'F':
        fruit+=1
        prodamount-=1
        costfruit += float(input("What is the cost of the product? "))
    elif category.upper() == 'B':
        beverage+=1
        prodamount-=1
        costbever += float(input("What is the cost of the product? "))
    else:
        print("wrong input, try again")

if vegetables != 0:
    vegname = 'Vegetable'

if fruit != 0:
    fruitname = 'Fruit'

if beverage != 0:
    bevername = 'Beverage'


        







try:
    give_ticket_by_category(vegname, costveg, vegetables)
except:
    pass

try:
    give_ticket_by_category(fruitname, costfruit, fruit)
except:
    pass

try:
    give_ticket_by_category(bevername, costbever, beverage)
except:
    pass