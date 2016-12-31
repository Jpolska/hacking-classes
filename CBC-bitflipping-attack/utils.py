import os

from Crypto.Cipher import AES

BS = 16  # Block size


class InvalidPadding(Exception):
    pass


def enhex(text):
    return text.encode("hex")


def unhex(text):
    return text.decode("hex")


def pad(text):
    padding_size = BS - len(text) % BS
    text += chr(padding_size) * padding_size
    return text


def unpad(text):
    padding_size = ord(text[-1])
    # If any of the last padding_size characters of text differs from
    # padding_size then raise padding error
    if filter(lambda x: ord(x) != padding_size, text[-padding_size:]):
        raise InvalidPadding('Invalid PKCS#7 padding')
    return text[:-padding_size]


def XOR(s1, s2):
    assert(len(s1) == len(s2))
    return ''.join(chr(ord(s1[x]) ^ ord(s2[x])) for x in range(len(s1)))


def chunk(text):
    return [text[i:i + BS] for i in range(0, len(text), BS)]


def merge_chunks(chunks):
    return "".join(chunk for chunk in chunks)


def Encrypt_AES_CBC(msg, key, iv):
    msg = pad(msg)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return cipher.encrypt(msg)


def Decrypt_AES_CBC(ct, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg = cipher.decrypt(ct)
    return unpad(msg)
