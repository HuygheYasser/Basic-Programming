z = "600"
x = input("give x: ")
y = input("give y: ")

def addup(x: str, y: str) -> str:
    global z
    z += x + y
    return int(z)


print(f"the combined value + 600 is: {addup(x,y)}")