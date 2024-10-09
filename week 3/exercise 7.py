start = int(input("give first number (start value): "))
stepsize = int(input("give the step size (positive): "))
amount = int(input("give the amount of numbers to be printed: "))



def print_list_numbers(st: int, step: int, amou: int) -> int:
    print("The numbers you're looking for are: ")
    print(st)
    amou -= 1
    while amou != 0:
        amou -= 1
        st += step
        print(st)


print_list_numbers(start, stepsize, amount)

























# def print_list_numbers(st: int, step: int, amou: int) -> int:
#     print("The nums you are looking for are: ")
#     print(st)
#     amou -= 1
#     while amou != 0:
#         st += step
#         amou -= 1
#         print(st)




# print_list_numbers(start, stepsize, amount)