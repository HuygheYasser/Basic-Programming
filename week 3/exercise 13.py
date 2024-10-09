def swap(a: str, b: str) -> str:
    return f"{b[:2]}{a[2:]} {a[:2]}{b[2:]}"



aa = input("Give a word: ")
bb = input("Give another word: ")


print(swap(aa, bb))
