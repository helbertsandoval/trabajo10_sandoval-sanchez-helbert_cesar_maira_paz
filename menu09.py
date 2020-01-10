import libreria
#1.implementacion del sub menu
def vino():
    contenido=(input("¿Cuantas veces al mes consume?:"))+ "\n"
    libreria.guardar_datos("Tienda", contenido, "a")


def cerveza():
    contenido=(input("¿Cuantas veces al mes consume?"))+ "\n"
    libreria.guardar_datos("Tienda", contenido, "a")

def wisky():
    contenido=(input("¿Cuantas veces al mes consume?")) + "\n"
    libreria.guardar_datos("Tienda", contenido, "a")

#menu de comandos
opc=0

max=4
while(opc != max):
    print("##### LA TABERNA ####")
    print("1. vino")
    print("2. Cerveza")
    print("3. Wisky")
    print("4. No Tomo")
    opc=libreria.pedir_numero("Escoja su producto preferido:", 1, 4)
    #mapeo de las opciones
    if (opc == 1):
        vino()
    if (opc == 2):
        cerveza()
    if (opc == 3):
        wisky()

print("Gracias"+"\n"+ "Tomar bebidas alcoholicas en exceso es dañino")
