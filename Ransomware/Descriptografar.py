from cryptography.fernet import Fernet #Lib to crypto
import os #Navegate into files and folders

def load_key():
    return open("key.key", "rb").read()

def descrypto_file(file, key):
    f = Fernet(key)
    with open(file, "rb") as filed:
        data = filed.read()
        data_descrypto = f.decrypt(data)
    with open(file, "wb") as file:
        file.write(data_descrypto)

def find_files(folder):
    list = []
    for root, _, files in os.walk(folder):
        for name in files:
            path = os.path.join(root, name)
            if name != "ransomware.py" and not name.endswith(".key"):
                list.append(path)
    return list

def main():
    key = load_key()
    files = find_files("Test_Files")
    for file in files:
        descrypto_file(file, key)
    print("Arquivos restaurados com sucesso")

if __name__ == "__main__":
    main()
