import libreria
#1.implementacion del sub menu
def colegio():
    contenido=(input("ingrese nombre:"))+ "\n"
    libreria.guardar_datos("centros_educativos.txt", contenido, "a")
    print("Datos guardados")

def universidad():
    contenido=(input("ingrese nombre:")) + "\n"
    libreria.guardar_datos("centros_educativos.txt", contenido, "a")
    print("Datos guardados")
def instituto():
    contenido=(input("ingrese nombre:")) + "\n"
    libreria.guardar_datos("centros_educativos.txt", contenido, "a")
    print("Datos guardados")


#menu de comandos
opc=0

max=4
while(opc != max):
    print("##### MENU ####")
    print("1. colegio")
    print("2. universidad")
    print("3. instituto")
    print("4. salir")
    opc=libreria.pedir_numero("ingrese una opcion:", 1, 4)
    #mapeo de las opciones
    if (opc == 1):
        colegio()
    if (opc == 2):
        universidad()
    if (opc == 3):
        instituto()

print("gracias")
