import libreria
#1. Implementacion de submenu
def agregarTrabajo():
    #1.pedir la fuerza
    #2. pedir la distancia
    #3.hallar el trabajo
    fuerza=libreria.pedir_numero("ingrese la fuerza",5,490)
    distancia=libreria.pedir_numero("ingrese la distancia",1, 400)
    print("ingrese el trabajo", fuerza*distancia)

def agregarFuerza():
    #1. pedir la masa
    #2. pedir la aceleracion
    #3. calcular la fuerza
    masa=libreria.pedir_numero("ingrese la masa",10,350)
    aceleracion=libreria.pedir_numero("ingrese la aceleracion",3,200)
    print("ingrese la fuerza", masa*aceleracion)
# Menu de comandos
opc=0
max=3
while(opc!= max):
    print("############### MENU ##############")
    print("#1. agregar trabajo")
    print("#2. opcion fuerza")
    print("#3. Salir ")
    #2. Eleccion de la opcion menu
    opc=libreria.pedir_numero("Ingreso la opcion:", 1, 3)
    #3. Mapeo de las opciones
    if (opc==1):
        agregarTrabajo()
    if (opc==2):
        agregarFuerza()
