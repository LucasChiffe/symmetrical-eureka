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
    