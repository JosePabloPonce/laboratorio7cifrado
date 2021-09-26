#------------MCD EUCLIDES----------
def mcdEuclides(n1, n2):
    
    while n1 % n2 != 0:
        sobrante = n1 % n2
        n1 = n2
        n2 = sobrante
        
    return n2

print("MCD utilizando el algoritmo de Euclides") 
print("Para 1036 y 240 el resultado es:", mcdEuclides(1036, 240))
print("Para 22896 y 192 el resultado es:", mcdEuclides(22896, 192))
print("Para 689161 y 378851 el resultado es:", mcdEuclides(689161, 378851))


#------------MCD EUCLIDES EXTENDIDO----------
def euclidesExtendido(n1, n2):
    x,y, u,v = 0,1, 1,0
    while n1 != 0:
        q, r = n2//n1, n2%n1
        m, n = x-u*q, y-v*q
        n2,n1, x,y, u,v = n1,r, u,v, m,n
    mcd = n2
    return mcd, x, y

print("-------------------------------------------------------------------")
print("Algoritmo de Euclides Extendido")
print("El primer valor corresponde al mcd, seguido de los valores de x y y")
print("Para 1036 y 240 el resultado es:" ,euclidesExtendido(1036,240))
print("Para 8753 y 3354 el resultado es:" ,euclidesExtendido(8753,3354))
print("Para 2021 y 43 el resultado es:" ,euclidesExtendido(2021,43))


#------------Fermat Test----------
import numpy as np
import matplotlib.pyplot as plt


import numpy as np
import matplotlib.pyplot as plt

numerosGenerados = 0

def fermatTest(n, k):
    isprime= True
    witness= []
    for i in range(0, k):
        a = np.random.randint(2, n)
        an = pow(a, (n-1)) %n
        witness.append(a)
        if (an != 1):
            isprime = False
            break
    #print(isprime)
    if isprime:
        #print('witness: {}'.format(witness))
        return(True, n)
    else:
       # print('liar: {}'.format(a))
        return(False, n)


def generador(longitud):
    numero='20'
    for i in range(longitud-2):
        numero+= str(np.random.randint(0, 10))

    return(int(numero))

print("-------------------------------------------------------------------")
print("Fermat Test")
fermatTest(11, 5)


while (numerosGenerados<5):
    resultado = fermatTest(generador(5), k=5)
    if(resultado[0] == True):
        print(resultado[1])
        numerosGenerados+=1
