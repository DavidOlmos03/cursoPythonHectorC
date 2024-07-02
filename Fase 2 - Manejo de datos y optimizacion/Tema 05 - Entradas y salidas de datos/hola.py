import sys

# accedo a la dirección o ruta del fichero
# ['c:\\Users\\juand\\Documents\\Projects\\Python\\CursoPython\\Fase 2 - Manejo de datos y optimizacion\\Tema 05 - Entradas y salidas de datos\\hola.py']     
# print(sys.argv)

for argumento in sys.argv[1:]:
    print(argumento)