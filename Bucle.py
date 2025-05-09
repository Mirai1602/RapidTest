"""
Autor: Mayrin Tellez
Version: 1.0
Fecha: 09-05-25
Descripcion: Solicita un numero positivo y muestra todos los numeros pares desde dos 
hasta ese numero
"""
def contarPares():

    lin= int(input("Digite el numero limite: "))
    cont =0
    while (cont <= lin):
        if(cont % 2 ==0 ):
            print(f"{cont} Es un numero par")
        cont += 1 #Solo asi se puede incrementar la variable en python 
    print("--------------------------------------")
    print(f"{cont} Es mayor o igual a {lin}")
