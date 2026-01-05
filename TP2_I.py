def nbPremiers(lim):
    premiers = []
    for n in range(2, lim):
        est_premier = True
        for x in range(2, int(n**0.5) + 1):
            if n % x == 0:
                est_premier = False
                break
        if est_premier:
            premiers.append(n)
    return premiers


def decompPrimaire(nombre):
    decomp = []
    puissance = []

    premiers = nbPremiers(nombre // 2)

    for x in premiers:
        if nombre == 1:
            break

        compteur = 0
        while nombre % x == 0:
            compteur += 1
            nombre //= x

        if compteur > 0:
            decomp.append(x)
            puissance.append(compteur)

    return decomp, puissance

def phi(nombre):
    nbr=decompPrimaire(nombre)
    result=1
    for i in range(len(nbr[0])):
        if nbr[1][i] == 1:
            result*=nbr[0][i]-1
        else:
            result*=nbr[0][i]**(nbr[1][i])-nbr[0][i]**(nbr[1][i]-1)
    return result

"""print(decompPrimaire(1500))
print(phi(1500))
print(phi(phi(1500)))"""