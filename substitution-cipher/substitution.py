import random
import string


def shuffle(s):
    return ''.join(random.sample(s, len(s)))


def GetRandomSub():
    alphabet = string.uppercase
    sub = {}
    for l, m in zip(alphabet, shuffle(alphabet)):
        sub[l] = m
    return sub


def Encrypt(text, sub):
    out = ""
    for l in text:
        if l in sub:
            out += sub[l]
        else:
            out += l
    return out

sub = GetRandomSub()
text = open("flag.txt").read()
with open("ciphertext.txt", 'w') as outf:
    outf.write(Encrypt(text, sub))
