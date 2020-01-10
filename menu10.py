import libreria
#1.implementacion del sub menu
def coca():
    contenido=(input("¿Cuantas veces al mes consume?:"))+ "\n"
    libreria.guardar_datos("bakus", contenido, "a")
    recomienda_consumo=""
    while(recomienda_consumo != "si" and recomienda_consumo != "no"):
        recomienda_consumo=input("¿recomienda su consumo(si/no)?")
        libreria.guardar_datos("bakus", contenido, "a")


def pepsi():
    contenido=(input("¿Cuantas veces al mes consume?"))+ "\n"
    libreria.guardar_datos("bakus", contenido, "a")
    recomienda_consumo=""
    while(recomienda_consumo != "si" and recomienda_consumo != "no"):
        recomienda_consumo=input("¿recomienda su consumo(si/no)?")
        libreria.guardar_datos("bakus", contenido, "a")

def inka():
    contenido=(input("¿Cuantas veces al mes consume?")) + "\n"
    libreria.guardar_datos("bakus", contenido, "a")
    recomienda_consumo=""
    while(recomienda_consumo != "si" and recomienda_consumo != "no"):
         recomienda_consumo=input("¿recomienda su consumo(si/no)?")
         libreria.guardar_datos("bakus", contenido, "a")

def agua():
    recomienda_consumo=""
    while(recomienda_consumo != "si" and recomienda_consumo != "no"):
        recomienda_consumo=input("¿recomienda su consumo(si/no)?")
        libreria.guardar_datos(("bakus", contenido, "a"))
#menu de comandos
opc=0

max=5
while(opc != max):
    print("##### bakus ####")
    print("1. Coca cola")
    print("2. Pepsi")
    print("3. Inka cola")
    print("4. Agua")
    print("5. No deseo porticipar en la encuesta")
    opc=libreria.pedir_numero("Escoja su producto preferido:", 1, 5)
    #mapeo de las opciones
    if (opc == 1):
        coca()
    if (opc == 2):
        pepsi()
    if (opc == 3):
        inka()
    if (opc == 4):
        agua()


print("Gracias")
