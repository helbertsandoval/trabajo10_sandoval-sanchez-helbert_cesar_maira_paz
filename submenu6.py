import libreria
#1. Implementacion de submenu
def agregarAreadelrectangulo():
    #1 agregamos la base del rectangulo
    #2 agregamos la altura del rectangulo
    #3. calculamos el area del rectangulo
    base=libreria.pedir_numero("ingrese la base",3,300)
    altura=libreria.pedir_numero("ingrese la altura",2,500)
    print("ingrese el area del rectangulo", base*altura)
def agregarAreadelcuadrado():
    #1 agregamos el lado del cudrado
    #2 hallamos el area del cuadrado
    lado=libreria.pedir_numero("ingrese el lado:",2,10)
    print("ingrese el area del cuadrado", lado**2)
# Menu de comandos
opc=0
max=3
while(opc!= max):
    print("############### MENU ##############")
    print("#1. agregar el area del rectangulo")
    print("#2. agreegar el area del cuadrado")
    print("#3. Salir ")
    #2. Eleccion de la opcion menu
    opc=libreria.pedir_numero("Ingreso la opcion:", 1, 3)
    #3. Mapeo de las opciones
    if (opc==1):
        agregarAreadelrectangulo()
    if (opc==2):
        agregarAreadelcuadrado()
