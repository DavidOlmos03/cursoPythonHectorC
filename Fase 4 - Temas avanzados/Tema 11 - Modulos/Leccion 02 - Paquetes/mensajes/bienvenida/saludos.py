def saludar():
    print("Hola. te saludo desde saludos.saludar()")

def prueba():
    print("Esto es una prueba de la nueva versión")
    
class Saludo:
    def __init__(self):
        print("Hola te saludo desde Saludo.__init__")


# Esta variable __name__ almacena el nombre del script en el que me encuentro, entonces lo que este aqui solo se va a ejecutar si ejecuto
# directamente el script en cuestion, cuando ejecuto el script directamente __name__ == '__main__' desde otro lugar __name__ == 'saludos'
# print(__name__)
if __name__ == '__main__':
    saludar()