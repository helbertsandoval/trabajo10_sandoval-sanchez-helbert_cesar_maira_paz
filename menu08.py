import libreria
#1.implementacion del sub menu
def avemicina():
    contenido=(input("¿Por que prefiere este producto?:"))+ "\n"
    libreria.guardar_datos("purina.txt", contenido, "a")


def papeadito():
    contenido=(input("¿Por que prefiere este producto?")) + "\n"
    libreria.guardar_datos("purina.txt", contenido, "a")


def engorde():
    contenido=(input("¿Por que prefiere este producto?")) + "\n"
    libreria.guardar_datos(("purina.txt", contenido, "a"))

#menu de comandos
opc=0

max=3
while(opc != max):
    print("##### Purina ####")
    print("1. avemicina")
    print("2. papeadito")
    print("3. engorde")
    print("3. Ninguno")
    opc=libreria.pedir_numero("Escoja su producto preferido:", 1, 3)
    #mapeo de las opciones
    if (opc == 1):
        avemicina()
    if (opc == 2):
        papeadito()
    if (opc == 3):
        engorde()

print("Purina sigue creciendo para usted")
