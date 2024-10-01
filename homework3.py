trousers = int(input("how many trousers have been bought? "))
tshirts = int(input("how many t-shirts have been bought? "))
vests = int(input("how many vests have been bought? "))

trprice = 70.5
tsprice = 20.89
veprice = 100.3


total = trousers*trprice + tshirts*tsprice + vests*veprice


print(f"You have bought \n\tTrousers: {trousers} pair(s)\n\tT-shirts: {tshirts} piece(s)\n\tVests: {vests} piece(s)\nTotal: {total}")