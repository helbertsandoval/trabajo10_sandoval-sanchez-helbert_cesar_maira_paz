import libreria
#1. Implementacion de submenu
def agregarDistancia():
    #1.pedir la velocidad
    #2.pedir el tiempo
    #3.calculando la distancia

    velocidad=libreria.pedir_numero("ingrese la velocidad",5,200)
    tiempo=libreria.pedir_numero("ingrese el tiempo",5, 100)
    print("la distancia", velocidad*tiempo)
def opcionTiempo():
    #1. pedir la distancia
    #2 pedir la velocidad
    #3 calcuar el tiempo
    distancia=libreria.pedir_numero("ingrese la distancia",200,350)
    velocidad=libreria.pedir_numero("ingrese la velocidad",100,200)
    print("ingrese el tiempo", distancia/velocidad)
# Menu de comandos
opc=0
max=3
while(opc!= max):
    print("############### MENU ##############")
    print("#1. agregar distancia")
    print("#2. opcion tiempo")
    print("#3. Salir ")
    #2. Eleccion de la opcion menu
    opc=libreria.pedir_numero("Ingreso la opcion:", 1, 3)
    #3. Mapeo de las opciones
    if (opc==1):
        agregarDistancia()
    if (opc==2):
        opcionTiempo()

#fin_menu

