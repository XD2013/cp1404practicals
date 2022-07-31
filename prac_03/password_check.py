def main():
    MINIMUM_LENGTH = 5

    password = input("Create your password (minimum length: 5): ")
    password = get_password(MINIMUM_LENGTH, password)
    asterisks = get_asterisk(password)
    print(f"Your password: {asterisks}")

def get_asterisk(password):
    asterisks = len(password) * "*"
    return asterisks

def get_password(MINIMUM_LENGTH, password):
    while len(password) < MINIMUM_LENGTH:
        print("Invalid password. The minimum length of password is 5.")
        password = input("Create your password (minimum length: 5): ")
    return password

main()