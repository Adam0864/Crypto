def binaire(n):
    return list(bin(n)[2:])


print(binaire(5))

def reste_puissance(x,p,n):
    p_bin=binaire(p)
    reste=1
    for i in range(len(p_bin)):
        if p_bin[len(p_bin)-1-i] == '1':
            reste*=(x**(2**i))%n
    reste=reste%n
    return reste

print(reste_puissance(2,17,55))