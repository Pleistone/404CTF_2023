from math import floor, ceil

values = [
    [35329, 87961, 42776, 17234],
    [100914, 40542, 19862, 49274],
    [67347, 27099, 61221, 152553],
    [122890, 49360, 18857, 46721],
    [147438, 59202, 25080, 62232],
    [58164, 144852, 27661, 68683],
    [135810, 54540, 128064, 51438],
    [54563, 135833, 98394, 39570],
    [51973, 129373, 66114, 26640],
    [144847, 58159, 25071, 62223],
    [35402, 88034, 57633, 143547],
    [17228, 42770, 43078, 107320],
    [64773, 26073, 25556, 63482],
    [115125, 46239, 27627, 68649],
    [35842, 89248, 26019, 64719],
    [29161, 72505, 39501, 98325]
]

n = len(values)

def solve(a,r11,r21,r12,r22):
    if (r11-r12)%(1-a)==0:
        return r11, (r11-r12)//(1-a)
    if (r11-r22)%(1-a)==0:
        return r11, (r11-r22)//(1-a)
    if (r21-r12)%(1-a)==0:
        return r21, (r21-r12)//(1-a)
    if (r21-r22)%(1-a)==0:
        return r21, (r21-r22)//(1-a)
    
    print("erreur")
    return 0


def find(a,r11,r21,r12,r22):
    r,c = solve(a,r11,r21,r12,r22)

    ascii_min = 33
    ascii_max = 128

    b1_sup = ascii_max
    b2_sup = ascii_max-c
    b3_sup = floor((r-ascii_min-c)/(a+1))
    b_sup = min(min(b1_sup,b2_sup), b3_sup)

    b1_inf = ascii_min
    b2_inf = ascii_min-c
    b3_inf = ceil((r-ascii_max-c)/(a+1))
    b_inf = max(max(b1_inf,b2_inf), b3_inf)

    if b_inf>b_sup:
        print("Pas de resultat")
 
    x2 = b_sup
    x1 = x2 + c 
    x0 = r - x1 - a*x2

    return [x0,x1,x2]

res = []
for r in values:
    res+=find(518,r[0],r[1],r[2],r[3])
print(res)

mdp = ""
for l in res:
    mdp = mdp + chr(l)
print(mdp)