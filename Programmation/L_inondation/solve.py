from pwn import remote

host = 'challenges.404ctf.fr'
port = 31420

def main():
   nc = remote(host, port)
   print(nc.readlineS())
   
   for k in range(100):
    res = ""
    for i in range(35):
       res+=nc.readlineS()
    print(res)
    print("round :",k)
    count_rhino = str(res.count(")"))
    print(count_rhino)
    nc.sendline(count_rhino.encode())

   for i in range(6):
      print(nc.readlineS())
main()
