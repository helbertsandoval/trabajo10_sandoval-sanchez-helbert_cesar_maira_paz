import libreria
#1. Implementacion de submenu
def opcionSumar():
    #1.pedir n1
    #2.pedir n2
    #3. calcular la suma :n1+n2
    n1=libreria.pedir_numero("ingrese n1:",1,100)
    n2=libreria.pedir_numero("ingrese n2:",1,50)
    print("la suma es:", n1+n2)
def opciondividir():
    #1 agregar n1
    #2. calcular la division: n1/6
    n1=libreria.pedir_numero("ingrese n1",1,80)
    print("dividir n1 entre 6 es:", n1/6 )
# Menu de comandos
opc=0
max=3
while(opc!= max):
    print("############### MENU ##############")
    print("#1. opcion sumar")
    print("#2. opcion dividir")
    print("#3. Salir ")
    #2. Eleccion de la opcion menu
    opc=libreria.pedir_numero("Ingreso la opcion:", 1, 3)
    #3. Mapeo de las opciones
    if (opc==1):
        opcionSumar()
    if (opc==2):
        opciondividir()

#fin_menu
