from TP2_I import *
from TP2_II import *
from TP2_III import *

def RSA(n,p,e,M):
    N=n*p
    mod = phi(N)
    d=inverse_modulaire(e,mod)
    while (d<0):
        d+=mod
    m_prime=reste_puissance(M,e,N)
    m_base=reste_puissance(m_prime,d,N)
    print(m_base)
    return m_prime

print(RSA(101,103,7,10331))