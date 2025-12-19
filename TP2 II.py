def bezout(a,b):
    L1=[a,1,0]
    L2=[b,0,1]
    while (L2[0]!=1):
        q = L1[0] // L2[0]
        L3=[L1[0]-q*L2[0],L1[1]-q*L2[1],L1[2]-q*L2[2]]
        L1,L2=L2,L3
    return L2[1],L2[2]

def inverse_modulaire(inverse,modulo):
    l = bezout(inverse,modulo)
    return l[0]
print(bezout(117,368))
print(inverse_modulaire(51,242))