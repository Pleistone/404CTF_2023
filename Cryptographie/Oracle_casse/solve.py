from Crypto.Util.number import long_to_bytes
from math import gcd

def find_facteur(n,e,v,c):
    facteur = gcd(n, pow(c,e,n)-v)
    return facteur 

def déchiffre(n,d,ct):
    res = pow(ct,d,n)
    return res

def main():
    n = 0xa08a7e773a543038a33e0374dcae5c9978195f5a83b320e7f0e04cf3fcd84075f1f86af3343b7a460c3802e5e4ec962527c164e9acc5e0d32064a6c32d814b724f073079120188699d27b5c10c52d43e2b9a3572db1ddb9d3e6e24a1213e1ddcb8a512f8ab610ef2ecf1fca725c62bfc39d3e9bbceafc2da34cc23f774e3ce4393c5f70949e533922aea7688c2e7b550eb126b88a4a558f62c53a26d3fb52308a345e4e6106455d3ac6191e508873692439762d8d6bd955f0f61192b849031f857cedceee729713fd307b1c12ab12384f04dbfad0580c322173439279ea3e715bf560052d04552ef51aa3d11ad94bf88129193ea1bf3237e4d0556b35ff4a2cb
    e = 0x10001
    v = 10
    c = 9476064908862563624120163863826079080053004349754282462261712758336955350400383866925198564632731637600565820151806277786085330844830267618763590414551248363955138540101581578791605270814454492191605764826159831751833054229359083607231067909633310167103438450735979885268374630037435235109700957751675939089589596314562742694368767040664658251861358058982921877987057575874323416216919072176209365051241747009089066869320137334327660165955299639799859027211278352696885661019046335385562102562486021956380836154509979822704305232544167910336930120306974138341307835203198524678483658524097431638405006044699937757815

    p = find_facteur(n,e,v,c)
    q = n//p
    d = pow(e, -1, (p-1) * (q-1))
    ct = 16436408794500600748720095384311310457785682452535399228804364667399010493694723414880767030577197207141596152732647320548633067418674126197409411468516593612490322953675740462939338468808083184194580108733434278503808378653769995773826982238745428954665042191988689009510739813802566555142501166830820212416981219951891109455538470558353329947398943921118327338295103640714260344689665889155923816960096588458452135264114079285142341828763935330947189029287864470247675808720768916907790853138405043774103885282860620355679338248546207911874518613537594341671566601177696984614145252936171616363523999041895734151696
    res = déchiffre(n,d,ct)
    flag = long_to_bytes(res)
    print(flag)

main()

