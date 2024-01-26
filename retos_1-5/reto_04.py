# /*
#  * Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.
#  */

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    if (num == 1):
        pass    
    else:
        print("Es primo --> "+str(num))
    return True


# es_primo(1)

for n in range(1,100):
    es_primo(n)