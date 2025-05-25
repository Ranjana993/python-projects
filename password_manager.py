from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key" ,"wb") as key_file:
        key_file.write(key)

write_key()
'''

def load_key():
    file = open("key.key" , "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    try:
        with open("passwords.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                if "|" in data:
                    user, passw = data.split("|", 1)
                    print("user:", user, "password:", fer.decrypt(passw.encode()).decode())
    except FileNotFoundError:
        print("No passwords found. Please add a password first.")

def add():
    name = input("Enter your account name: ")
    pwd = input("Enter your password: ")
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")




while True:
    mode = input("Would you like to add a new password or view existing passwords? (add/view) Or enter q to quit: ").lower()
    if mode == "q":
        print("Exiting the password manager.")
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. Please enter 'add' or 'view'.")