import sys

try:
    number = sys.argv[1]
    for i in range(len(str(number))):
        number2 = int(f"{number[-(i+1):]}")
        print(f"{number2:0{len(str(number))}d}")
except ValueError:
    print("Ocurrio un error")
