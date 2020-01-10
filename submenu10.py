import libreria
#1. Implementacion de submenu
def agregarPresion():
    #1 agregar la fuerza
    #2 agregar el area
    #3 calcular la presion en la cual equivale presion=fuerza/area
    fuerza=libreria.pedir_numero("ingrese la fuerza",20,180)
    area=libreria.pedir_numero("ingrese el area",5, 90)
    print("ingrese la presion",fuerza/area)

def agregarFrecuencia():
    #1 agregar el numero de vueltas
    #2. agregamos el tiempo
    #3. hallamos la frecuencia correspondida
    numero_de_vueltas=libreria.pedir_numero("ingrese el numero de vueltas",80,450)
    tiempo=libreria.pedir_numero("ingrese el tiempo",1,75)
    print("ingrese la frecuencia", numero_de_vueltas/tiempo)
# Menu de comandos
opc=0
max=3
while(opc!= max):
    print("############### MENU ##############")
    print("#1. agregar la presion")
    print("#2. agregar la frecuencia")
    print("#3. Salir ")
    #2. Eleccion de la opcion menu
    opc=libreria.pedir_numero("Ingreso la opcion:", 1, 3)
    #3. Mapeo de las opciones
    if (opc==1):
        agregarPresion()
    if (opc==2):
        agregarFrecuencia()
