import libreria
#1.implementacion del sub menu
def agregar_almuerzo():
    cantidad=libreria.pedir_numero("ingrese la cantidad de almuerzos:",0, 100)
    print("la cuenta esparcial es:",cantidad*80)

def agregar_cena():
    cantidad=libreria.pedir_numero("ingrese la cantidad de cenas:", 0, 100)
    print("la cuenta es parcial es:", cantidad*20)

#menu de comandos
opc=0

max=3
while(opc != max):
    print("##### MENU ####")
    print("1. zapatos")
    print("2. sandalias")
    print("3. salir")
    opc=libreria.pedir_numero("ingrese una opcion:", 1, 3)
    #mapeo de las opciones
    if (opc == 1):
        agregar_almuerzo()
    if (opc == 2):
        agregar_cena()
print("gracias por su compra")
