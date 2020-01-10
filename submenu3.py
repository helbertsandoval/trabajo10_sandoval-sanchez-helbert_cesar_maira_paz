import libreria
#1. Implementacion de submenu
def opcionRestar():
    #1. pedir n1
    #2 pedir n2
    #3. cacular la resta entre n1-n2
    n1=libreria.pedir_numero("ingrese n1:",1,180)
    n2=libreria.pedir_numero("ingrese n2:",1,110)
    print("la resta es:", n1-n2)
def opcionMultiplicar():
    #1.agregar n1
    #2 cacular la multiplicacio:n1*2
    n1=libreria.pedir_numero("ingrese n1",1,80)
    print("multiplicar n1 *2 es:", n1*2 )
# Menu de comandos
opc=0
max=3
while(opc!= max):
    print("############### MENU ##############")
    print("#1. opcion restar")
    print("#2. opcion multiplicar")
    print("#3. Salir ")
    #2. Eleccion de la opcion menu
    opc=libreria.pedir_numero("Ingreso la opcion:", 1, 3)
    #3. Mapeo de las opciones
    if (opc==1):
        opcionRestar()
    if (opc==2):
        opcionMultiplicar()

#fin_menu
