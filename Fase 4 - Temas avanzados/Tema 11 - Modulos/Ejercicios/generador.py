import random
import math
def leer_numero(ini, fin, mensaje):
    while True:
        try:
            num = int(input(mensaje))
        except:
            pass
        else:
            if num >= ini and num <= fin:
                break
        
    return num


def generador():
    numeros = leer_numero(1,20,"¿Cuantos números quieres generar? [1-20]:")
    modo = leer_numero(1,3,"¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal:")

    lista = []
    for i in range(numeros):
        numero = random.uniform(0,100)
        print("Numero normal: ", numero)

        if modo == 1:
            lista.append(math.ceil(numero))
            print("Numero redondeo: ", lista[i])
        if modo == 2:
            lista.append(math.floor(numero))
            print("Numero redondeo: ", lista[i])
        if modo == 3:
            lista.append(numero)
            print("Numero redondeo: ", lista[i])

    return lista

generador()
