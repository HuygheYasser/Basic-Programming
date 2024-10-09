def generate_password(first: str, last: str, birth: str):
    print(f"{last[:3]}{first[:2]}{birth[3:5]}{birth[6:8]}")


lastname = input("Give last name: ")
firstname = input("Give first name: ")
birthday = input("Give birthday (dd-mm-yyyy): ")


generate_password(firstname, lastname, birthday)