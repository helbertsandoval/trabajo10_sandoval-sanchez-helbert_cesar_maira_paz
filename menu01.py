import libreria
#1.implementacion del sub menu
def agregar_almuerzo():
    cantidad=libreria.pedir_numero("ingrese la cantidad de almuerzos:",0, 100)
    cuenta_parcial = cantidad*8
    print("la cuenta es:",cuenta_parcial)

def agregar_cena():
    cantidad=libreria.pedir_numero("ingrese la cantidad de cenas:", 0, 100)
    cuenta_parcial = cantidad*5
    print("la cuenta es:", cuenta_parcial)

#menu de comandos
opc=0

max=3
while(opc != max):
    print("##### MENU ####")
    print("1. almuerzo 8$")
    print("2. cena 5$")
    print("3. salir")
    opc=libreria.pedir_numero("ingrese una opcion:", 1, 3)
    #mapeo de las opciones
    if (opc == 1):
        agregar_almuerzo()
    if (opc == 2):
        agregar_cena()
print("gracias por su compra")
