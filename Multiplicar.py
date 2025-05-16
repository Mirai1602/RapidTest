"""
Autor:Mayrin Tellez
Fecha: 16/05/2025
Version: 1.0
Descripcion: Escribe un progrma que muestre la 
tabla de multiplicar del numero n, desde 1 hasta n
"""
import os 
def multiplicar(): 
    print("*******TABLA DE MULTIPLICACION**********")
    n = int(input("Digite un numero base de la tabla: "))
    m=int(input("Digite el numero limite multiplicador: "))
    os.system("cls")
    print("----------------------------------------------")
    print(f"///////// TABLA DE MULTIPLICAR DE 1 HASTA {n} ////////////")
    for i in range(1, n+1, 1 ):
        for j in range(1, m+1, 2 ):
            print(f"{i} x {j} = {i*j}")
        print("\n")
    print("-----------------------------------------")
