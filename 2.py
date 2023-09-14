def CelaFag(Celcius):
    fah = (Celcius * 9/2) + 32  
    return fah
def FagCel(fahrenheit):
    Cel = (fahrenheit - 32) * 5/9
    return Cel
print("Seleccione una opción")
print("1) De Celsius a fahrenheit")
print("2) De fahrenheit a Celcius")
Opcion = int(input("Ingrese la opcion deseada: "))
if Opcion == 1:
    Celsius = int(input("Ingrese la cantidad de grados celcius que desea convertir a fahrenheit: "))
    Conver = CelaFag(Celcius)
    print(f"{Celsius} grados Celsius es igual a {Conver} grados fahrenheit")
elif Opcion == 2:
    fahrenheit = int(input("Ingrese la cantidad de grados fahrenheit que desea convertir a Celcius: "))
    Conver = FagCel(fahrenheit)
    print(f"{fahrenheit} grados Celsius es igual a {Conver} grados fahrenheit")
else:
        print("Los datos ingresados no pertenecen a las opciones dadas, intente nuevamente")