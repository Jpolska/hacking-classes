def recvuntil(sock, ending):
    buf = ""
    while not buf.endswith(ending):
        buf += sock.recv(1)
    return buf


def recvline(sock):
    return recvuntil(sock, "\n")[:-1]


def sendline(sock, buf):
    if not buf.endswith("\n"):
        buf += "\n"
    return sock.sendall(buf)
