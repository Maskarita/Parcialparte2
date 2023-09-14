inicio = int(input("Ingrese el número de inicio del rango: "))
final = int(input("Ingrese el número final del rango: "))

def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def encontrar_primos_en_rango(inicio, fin):
    primos = []
    numero = max(2, inicio)
    
    while numero <= fin:
        if es_primo(numero):
            primos.append(numero)
        numero += 1
    
    return primos

primos_en_rango = encontrar_primos_en_rango(inicio, final)

if len(primos_en_rango) > 0:
    print(f"Los números primos en el rango de {inicio} a {final} son: {primos_en_rango}")
else:
    print(f"No se encontraron números primos en el rango de {inicio} a {final}")