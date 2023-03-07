"""
Allen Jean encode code
"""

def encode(password):
    list_password = []
    for i in password:
        list_password.append(int(i) + 3)

    str_password = ""
    for j in list_password:
        str_password += str(j)

    return str_password


def decode(password):
    list_password = []
    for i in password:
        list_password.append(int(i) - 3)

    str_password = ""
    for j in list_password:
        str_password += str(j)

    return str_password


def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def main():
    print()
    menu()
    print()
    user_option = int(input("Please enter an option: "))
    while user_option != 3:
        if user_option == 1:
            orig_pwd = input("Please enter your password to encode: ")
            encoded = encode(orig_pwd)
            print("Your password has been encoded and stored!")
        elif user_option == 2:
            decoder = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoder}")
        else:
            break
        print()
        menu()
        user_option = int(input("Please enter an option: "))

if __name__ == "__main__":
    main()
