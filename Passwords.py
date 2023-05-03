
import base64
import typing
from cryptography.fernet import Fernet
 
print()
print("In this program you will have to introduce a username and a password for your account.")
print("Your data will be written in an external file with your password encrypted. You can decrypt it at the end of the program if you want.")
print("For decrypt the passwords, you will have to know the master password")
print()
print("In the next steps you must write a username and a password")

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:     #generate a file called key.key in write in bytes mode that will write
        key_file.write(key)                     #the key generated by Fernet

def load_key():
    file =  open("key.key", "rb")               #read de file called key.key in read in bytes mode
    key = file.read()
    file.close()
    return key

mast_pwd = "SirBarrufet"

key = load_key() + mast_pwd.encode()       #we have our key in bytes, so the master password must be in bytes too            
fer = Fernet(key)                           #initializing the encryption module

def create_file():
    file = open('data.txt', 'w')
    user = input("Write your username: ")
    pwd = input("Write your password: ")
    file.write(user+ " / "+fer.encrypt(pwd.encode()).decode())      #we use de decode to remove the bites shown when we print the password
    file.close

def new_data():
    file = open('data.txt', 'a')
    user = input("Write a new username: ")
    pwd = input("Write a new password: ")
    file.write('\n'+user+" / "+fer.encrypt(pwd.encode()).decode())
    file.close

def read_file():
    file = open('data.txt', 'r')
    print(file.read())
    file.close

def new_account():
    value = input("Do you want to introduce a new account? (yes/no) ")
    return (value)

def check_value(value):
    if (value == "yes" or value == "no"):
        type = True
    else:
        type = False
    return (type)

def write_pwd_decrypted(password, user):
    with open('data.txt', 'a') as file:
        file.write('\n'+user+" / "+str(password))
    
def decrypt():
    file = open('data.txt', 'r')
    for line in file:
        x = line.split("/ ")
        user = x[0]
        pwd = x[1]
        #result = base64.decode(fer.decrypt(pwd.encode()).decode())
        result = fer.decrypt(pwd.encode())
        write_pwd_decrypted(result, user)

#main
create_file()

while True:
    
    value1 = new_account()
    type1 = check_value(value1)
    
    while (type1 != True):
        print("Wrong answer, type it correctly!")
        value1 = new_account()
        type1 = check_value(value1)
    
    if value1 == "yes":
        new_data()
        read_file()
    else:
        value2 = input("Do you want to decrypt all the passwords? (yes/no) ")
        type2 = check_value(value2)

        if value2 == "yes":
            decrypt()
        
        exit("Have a nice day!")