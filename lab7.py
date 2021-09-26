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


fermatTest(11, 5)


while (numerosGenerados<5):
    resultado = fermatTest(generador(5), k=5)
    if(resultado[0] == True):
        print(resultado[1])
        numerosGenerados+=1
        

