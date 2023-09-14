def buscar_numero(arreglo, numero):
    if numero in arreglo:
        return arreglo.index(numero)
    else:
        return -1
entrada_arreglo = input("Escriba los numeros que desea arreglar: ")
arreglo = [int(x) for x in entrada_arreglo.split()]
Buscar = int(input("Ingrese el número que desea buscar: "))
Ubicacion = buscar_numero(arreglo, Buscar)
if Ubicacion != -1:
    print(f"El número {Buscar} fue encontrado en la posición {Ubicacion} del arreglo.")
else:
    print(f"El número {Buscar} no fue encontrado en el arreglo.")