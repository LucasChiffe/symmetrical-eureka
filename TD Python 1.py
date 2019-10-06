## TD1

#On commence par le début

#Euler 1

#même pas besoin de fonction, une procédure suffit

S=0
for i in range(1000):
    if i%3==0 or i%5==0 and i%3!=0:
        S+=i
        
#et là on demande la valeur de S


#Euler 2

U0=1
U1=2
U2=U0+U1
S=U1
while U2<4*10**6:
    U0=U1
    U1=U2
    U2=U1+U0
    if U2%2==0:
        S+=U2
        
#idem on demande la valeur de S


#Euler 3
def testpremier(n):
    for i in range(2,int(n**(1/2))+1):
                   if n%i==0:
                       return False
    return True
            
                   
nombre=600851475143
max=0
for i in range(2,int(nombre**(1/2))+1):
    if testpremier(i) and nombre%i==0:
        max=i
        while nombre%i==0:
            nombre=nombre/i
        
#et là on demande max...


#Euler 4
def listenombre(n):
     L=[int(i) for i in str(n)]
     return L
    
def palindrome(n):
    max=9009
    for i in range(0,n):
        for j in range(0,n):
            if listenombre(i*j)==listenombre(i*j)[::-1]:
                max=i*j
    return max


def testpalindrome(n):
    return listenombre(n)==listenombre(n)[::-1]
        

#Euler 5
for i in range(3724680961):
    
    
    
    
#bon on a une énorme liste de noms

#on commence par une fonction qui transforme tout en lettres minuscules

def minuscule(L):
    for i in range(len(L)):
        L[i]=L[i].lower()
    return L

#ça fonctionne on peut continuer

#ensuite par une fonction qui renvoie l'ordre alphabétique d'une lettre

def nombrealphab(c):
    return ord(c)-ord('a')+1
#ça c'est bon ça me donne le bon nombre

#il faut une fonction qui transforme une liste de listes de 1 car en liste de listes de nombres

def transforme_en_nombres(L):
    liste=[]
    for i in range(len(L)):
        liste.append([])
        for j in L[i]:
            liste[i].append(nombrealphab(j))
    return liste


#maintenant on veut transformer chaque nom en une liste de str de 1 car

def transforme_nom(string):
    L=[]
    for i in string:
        L.append(i)
    return L
#bon on transforme chaque mot en liste de str

def transforme_liste(L):
    liste_de_str=[]
    for i in L:
        liste_de_str.append(transforme_nom(i))
    return liste_de_str
#c'est bon on a provisoirement gagné

#maintenant à chaque sous-liste on fait correspondre la sous-liste des nombres
#bon le L.sort() nous sauve
#on trie direct la grosse liste avec L.sort()
#on a une grosse liste dans l'ordre alphabétique, on va transformer chacun de ses termes en nombre et on peut même multiplier direct

def valeur_liste(L):
    liste_des_valeurs=[]
    for i in range(len(L)):
        compteur=0
        for j in L[i]:
            compteur+=int(j)
        liste_des_valeurs.append(compteur*(i+1))
    return liste_des_valeurs

#bon là on a un truc pas super joli qui nous renvoie des listes de nombres
#on somme et on a gagné

def somme(L):
    somme=0
    for i in L:
        somme+=i
    return somme

#bon il ne reste qu'à tout emboîter

def fonction_qui_fait_tout(L):
    Liste=L.copy()
    Liste.sort()
    Liste=minuscule(Liste)
    Liste=transforme_liste(Liste)
    Liste=transforme_en_nombres(Liste)
    Liste=valeur_liste(Liste)
    Liste=somme(Liste)
    return Liste
    
    
#On passe à Euler numéro 55

#On va faire une fonction qui teste tout et ça ira bien
#Bon il faut déjà faire un truc qui inverse tous les nombres avant de les add

#on va faire ça autrement

def transforme_en_liste(n):
    liste=[]
    n=str(n)
    for i in n:
        liste.append(int(i))
    return liste

#on va faire un truc avec un compteur

def fonction_finale(n):
    compteur=0
    for i in range(1,n+1):
        comparaisona50=0
        n=i
        L=[]
        K=transforme_en_liste(n)
        for k in range len(K):  #Pourquoi il considère que c'est un string ???
            L.append(K[k]+K[::-1][k])
        while comparaisona50<50:
            if L[::-1]==L:
                compteur+=1
                break
            for j in range len(L):  #et là ???
                L[j]=L[j]+L[::-1][j]
            comparaisona50+=1
        return compteur
