import os 
def mult():
    print("BIenvenido a la tabla de multiplicar")
    n= int(input("Ingrese el numero que desea multiplicar: "))
    m= int(input("Ingrese el numero hasta donde llegara la tabla *ejmplo: hasta el 12: "))
    lim = int(input("Ingrese el numero hasta donde quiere ver las tablas"))
    inicio = 1

    for n in range(n, m + 1):  
        print(f"\n------ Tabla del {n} ------")
        for i in range(inicio, lim + 1):  
            print(f"{n} x {i} = {n * i}")

    print("-----------------------------------------")

