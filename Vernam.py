M="01111111"
cle="011"

def vernam(cle,M):
    Mp=""
    compt=0
    for x in M:
        if int(x)+int(cle[compt%len(cle)])==2:
            Mp+="0"
            compt+=1
        else:
            Mp+=str(int(x)+int(cle[compt%len(cle)]))
            compt+=1
    return Mp
mprime=vernam(cle,M)
print(mprime)
print(vernam(cle,mprime))