import datetime
import time
import os


# while(True):
#     os.system('cls')  # Limpiamos la pantalla
#     dt = datetime.datetime.now()
#     print( "{}:{}:{}".format( dt.hour, dt.minute, dt.second ) )
#     time.sleep(1)  # Esperar 1 segundo

def hora_actual():
    dt = datetime.datetime.now()
    hour = dt.hour
    minute = dt.minute
    second = dt.second
    # print("Desde hora_actual")
    return f'{hour}:{minute}:{second}'

class Reloj:
    def __init__(self):
        while True:
            os.system('cls')
            print(hora_actual())
            time.sleep(1)

Reloj()