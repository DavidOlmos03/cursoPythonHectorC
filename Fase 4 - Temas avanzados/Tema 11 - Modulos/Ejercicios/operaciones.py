import math

def suma(num1, num2):
    try:
        return num1 + num2
    except TypeError:
        return "Error: Tipo de dato no válido"
    # return math.fsum([num1, num2])


def resta(num1, num2):
    try:
        return num1 - num2
    except TypeError:
        return "Error: Tipo de dato no válido"
    # return math.fsum([num1,-num2])

def producto(num1, num2):
    try:
        return num1*num2
    except TypeError:
        return "Error: Tipo de dato no válido"
    
def division(num1, num2):
    try:
        return num1/num2
    except TypeError:
        return "Error: Tipo de dato no válido"
    except ZeroDivisionError:
        return "Error: No es posible dividir entre cero"
    

# if __name__ == '__main__':
#     resta()