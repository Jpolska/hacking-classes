import os
import socket
import threading

from networking import *
from utils import *

# TODO Make it different for every user
KEY = os.urandom(16)
IV = os.urandom(16)


def get_cookie(user_data):
    """ Truncate all ';' and '=', so user cannot just simply get
        admin access by giving user_data = 'admin=true'
    """
    user_data = user_data.replace(";", "").replace("=", "")
    return "comment1=cooking%20MCs;userdata=" + user_data + \
        ";comment2=%20like%20a%20pound%20of%20bacon"


def validate_admin(cookie):
    return ";admin=true;" in cookie


class SimpleCookieServer():

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            print '[+] Got connection from ' + address[0] + ":" \
                                             + str(address[1])
            client.settimeout(60)
            threading.Thread(target=self.listen_to_client,
                             args=(client, address)).start()

    def listen_to_client(self, c, addr):
        sendline(c, "Hello user, please insert your data:")
        user_data = recvline(c)
        cookie = get_cookie(user_data)
        enc_cookie = enhex(Encrypt_AES_CBC(cookie, KEY, IV))
        sendline(c, "Your cookie: " + enc_cookie)

        sendline(c, "I'm a cookie monster, gimme cookie!")
        try:
            enc_cookie = unhex(recvline(c))
        except TypeError:
            sendline(c, "Non-hexadecimal character found. Quiting...")
            c.close()
            exit()
        try:
            cookie = Decrypt_AES_CBC(enc_cookie, KEY, IV)
        except InvalidPadding:
            sendline(c, "You are tempering with the data. Quitting...")
            c.close()
            exit()
        if validate_admin(cookie):
            flag = open('flag.txt').read()
            sendline(c, "Welcome almighty admin!\nHere is your flag: " + flag)
        else:
            sendline(c, "You're not admin! Shoo shoo, go away!!!")

        c.close()


if __name__ == "__main__":
    port_num = input("Port? ")
    SimpleCookieServer('localhost', port_num).listen()
