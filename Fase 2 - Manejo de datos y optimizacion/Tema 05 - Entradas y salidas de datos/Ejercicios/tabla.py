
import sys
print(sys.argv)
try:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])
    if len(sys.argv) == 3:
        
            # print(sys.argv)
            # filas = sys.argv[1]
            # columnas = sys.argv[2]
            # if filas < 1 or filas > 9 or columnas < 1 or columnas > 9:
            #     error = "El número de filas o columas no es correcto"
            #     print(error)
            # elif filas == None or columnas == None:
            #     error = "Ingrese tanto el número de filas como el de columnas"
            #     print(error)
            # else:
            for i in range(filas):
                for j in range(columnas):
                    print(" * ", end='')
                print("")
                # break
    
            
except ValueError:
    print("Ingrese tanto el número de filas como el de columnas")