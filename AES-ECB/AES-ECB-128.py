# Your task is to obtain secret x stored on a server
import os

from Crypto.Cipher import AES

# These are secret values stored on the server you are trying to hack.
# You do NOT have access to it!!!
# --------------------------TOP SECRET------------------------------
KEY = os.urandom(16)
x = "RG8gdGhlIGdvZCBkYW1uIFZpZ2VuZXJlIQ==".decode("base64")
# ------------------------------------------------------------------

BS = 16  # Block size

# Divide the whole text into chunks, each containing
# block size number of chars (except the last one)


def chunk(text):
    return [text[i:i + BS] for i in range(0, len(text), BS)]


def pad(text):
    pl = BS - (len(text) % BS)
    return text + chr(pl) * pl


def unpad(text):
    return text[:-ord(text[-1])]


def enhex(text):
    return text.encode("hex")


def unhex(text):
    return text.decode("hex")


def EncryptECB(plaintext, key):
    assert len(key) == 16
    plaintext = pad(plaintext)
    obj = AES.new(key, AES.MODE_ECB)
    ciphertext = obj.encrypt(plaintext)
    return ciphertext

# You have access to this function


def Encrypt(message):
    message = unhex(message) + x
    ciphertext = EncryptECB(message, KEY)
    return enhex(ciphertext)

# #############SAMPLE CODE###############
message = enhex("Ala ma kota")
ciphertext = Encrypt(message)
print unhex(ciphertext)
# #######################################


# ############YOUR CODE##################


# #######################################
