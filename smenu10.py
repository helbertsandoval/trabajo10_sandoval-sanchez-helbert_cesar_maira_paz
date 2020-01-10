import libreria
#1. Implementacion de submenu
def opcionareacirculo():
    R=libreria.pedir_numero("El radio del circulo es:", 5 , 20)
    pi=libreria.pedir_numero("El valor del pi es:",0, 180)
    print ("El area del circulo es:", ((pi)*(R**2)) )
def opcionareacuadrado():
    L=libreria.pedir_numero("El lado es:"10, 15)
    print ("El area del cuadrado es:", L**2 )

# Menu de comandos
opc=0
max=3
while(opc!= max):
    print("############### MENU ##############")
    print("#1. Mostrar área del circulo ")
    print("#2. Mostrar área cuadrado ")
    print("#3. Salir")
    #2. Eleccion de la opcion menu
    opc=libreria.pedir_numero("Ingreso la opcion:", 1, 3)
    #3. Mapeo de las opciones
    if (opc==1):
        opcionareacirculo()
    if (opc==2):
        opcionareacuadrado()

    #fin_while
