import libreria
#1.implementacion del sub menu
def preg1():
    contenido=(input("¿Vives con tus padres?:"))+ "\n"
    libreria.guardar_datos("encuesta.bienestar", contenido, "a")


def preg2():
    contenido=(input("¿Quien es el jefe del hogar?")) + "\n"
    libreria.guardar_datos("encuesta.bienestar", contenido, "a")

def preg3():
    contenido =input ("¿Cuantas personas personas aportan economicamente al hogar?") + "\n"
    libreria.guardar_datos("encuesta.bienestar", contenido, "a")

def preg4():
    contenido=(input("¿Por que solicitas el comedor?")) + "\n"
    libreria.guardar_datos("encuesta.bienestar", contenido, "a")

#menu de comandos
opc=0

max=5
while(opc != max):
    print("##### ENCUESTA BIENESTAR UNIVERSITARIO ####")
    print("1. pregunta01")
    print("2. pregunta02")
    print("3. pregunta03")
    print("4. pregunta03")
    print("5. Finalizado")
    opc=libreria.pedir_numero("ingrese una opcion:", 1, 5)
    #mapeo de las opciones
    if (opc == 1):
        preg1()
    if (opc == 2):
        preg2()
    if (opc == 3):
        preg3()
    if (opc == 4):
        preg4()
print("¡Gracias!")
