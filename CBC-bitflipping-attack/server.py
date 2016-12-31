import os
import socket

from networking import *
from utils import *

KEY = os.urandom(16)
IV = os.urandom(16)


def get_cookie(user_data):
    """ Truncate all ';' and '=', so user cannot just simply get
        admin access by giving user_data = 'admin=true'
    """
    user_data = user_data.replace(";", "").replace("=", "")
    return "comment1=cooking%20MCs;userdata=" + user_data + ";comment2=%20like%20a%20pound%20of%20bacon"


def validate_admin(cookie):
    return ";admin=true;" in cookie


def accept_conn():
    c, addr = me.accept()
    print 'Got connection from', addr
    return c, addr


def main():
    c, addr = accept_conn()

    sendline(c, "Hello user, please insert your data:")
    user_data = recvline(c)
    cookie = get_cookie(user_data)
    enc_cookie = enhex(Encrypt_AES_CBC(cookie, KEY, IV))
    sendline(c, "Your cookie: " + enc_cookie)

    sendline(c, "I'm a cookie monster, gimme cookie!")
    enc_cookie = unhex(recvline(c))
    try:
        cookie = Decrypt_AES_CBC(enc_cookie, KEY, IV)
    except InvalidPadding:
        sendline(c, "You are tempering with the data...")
        c.close()
    if validate_admin(cookie):
        flag = open('flag.txt').read()
        sendline(c, "Welcome almighty admin!\nHere is your flag: " + flag)
    else:
        sendline(c, "You're not admin! Shoo shoo, go away!!!")

    c.close()

me = socket.socket()
host = "localhost"
port = 9999
me.bind((host, port))

me.listen(5)
while True:
    try:
        main()
    except:
        pass
