import sys

if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])

    for r in range(repeticiones):
        print(texto)

else:
    print("ERROR - introduce los argumentos correctamente")
    # Para escapar texto se utiliza la estructura \"texto_a_escapar\", asi ase pueden mostrar las comillas dobles en la respuesta 
    print("Ejemplo: escribir_lineas.py \"Texto\" 5")