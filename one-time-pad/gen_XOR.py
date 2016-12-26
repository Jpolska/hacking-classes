from random import randint


def GenRandStr(n):
    return "".join(chr(randint(0, 255)) for x in range(n))


def stob(s):
    out = ''
    for ch in s:
        out += bin(ord(ch))[2:] + " "
    return out


def xor(a, b):
    assert len(a) == len(b)
    return "".join(chr(ord(a[x]) ^ ord(b[x])) for x in range(len(a)))

p1 = "######"
p2 = "######"
key = GenRandStr(6)

c1 = stob(xor(p1, key))
c2 = stob(xor(p2, key))

print c1
print c2
