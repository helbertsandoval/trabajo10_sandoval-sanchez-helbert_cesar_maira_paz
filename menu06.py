import libreria
#1.implementacion del sub menu
def navidad():
    contenido=(input("¿Cual es la palabra clave navideña?:"))+ "\n"
    libreria.guardar_datos("caliente.txt", contenido, "a")


def ano_n():
    contenido=(input("Ingresa la palabra clave de año nuevo")) + "\n"
    libreria.guardar_datos("caliente.txt", contenido, "a")

#menu de comandos
opc=0

max=3
while(opc != max):
    print("##### PERIODICO CALIENTE ####")
    print("1. paticipar del sorteo navideño")
    print("2. participar del sorteo año nuevo")
    print("3. Finalizado")
    opc=libreria.pedir_numero("ingrese una opcion:", 1, 3)
    #mapeo de las opciones
    if (opc == 1):
        navidad()
    if (opc == 2):
        ano_n()
print("¡SI TE INSCRIBES TODOS LOS DIAS HAY MAS OPCIONES DE GANAR!")
print("si el registro de la palabra es incorrecto no serás tomado en cuenta")
