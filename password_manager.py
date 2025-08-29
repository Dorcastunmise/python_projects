from cryptography.fernet import Fernet # allows encryption and decryption of passwords


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file: #write in byte mode - a file format (wb) ...write into a file
        key_file.write(key)
    return key


def load_key():
    with open("key.key", "rb") as key_file: #read in byte mode
        key = key_file.read()
        return key
    
pwd = input("Type in the master password for the server: ")
'''key = write_key() + pwd.encode()
Reason: Fernet keys must be exactly 32 url-safe base64-encoded bytes. You can't just append your password.
'''
key = write_key()
fer = Fernet(key)

read = load_key() + pwd.encode()  #encode the password to bytes
fer_read = Fernet(read)

def add():
    name = (input("Enter the name of the account: ")).strip()
    password = (input("Enter the password for the account: ")).strip()

    with open('passwords.txt', 'a') as f:
        f.write(f"{name}:{fer.encrypt(password.encode()).decode()}\n")

def retrieve():
    name = (input("Enter the name of the account to retrieve: ")).strip()
    with open('passwords.txt', 'r') as f:
        for line in f:
            if line.startswith(name + ":"):
                pwrd = line.strip().split(':')[1]
                print(f"Retrieved account for {name} with the password: {fer_read.decrypt(pwrd.encode()).decode()}")
                return
    print(f"No account found for {name}.")



while True:
    mode = input("Would you like to add a new password, retrieve existing ones or quit? (add/retrieve/quit): ").strip().lower()
    if mode == 'retrieve':
        retrieve()
    elif mode == "add":
        add()
    elif mode == "quit":
        print("Exiting the password manager.")
        break
    else:
        print("Invalid mode selected.")
        continue