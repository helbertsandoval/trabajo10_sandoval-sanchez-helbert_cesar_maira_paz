import libreria
#1.implementacion del sub menu
def incapaz():
    contenido=(input("¿Estas conforme con la gestion del rector?¿Por que?:"))+ "\n"
    libreria.guardar_datos("encuesta.txt", contenido, "a")


def profesor():
    contenido=(input("Menciona al profesor que siempre es puntual:")) + "\n"
    libreria.guardar_datos("encuesta.txt", contenido, "a")

def opinion():
    contenido=(input("¿Como crees que podria mejorar la unprg?:")) + "\n"
    libreria.guardar_datos("encuesta.txt", contenido, "a")



#menu de comandos
opc=0

max=4
while(opc != max):
    print("##### ENCUESTA UNPRG ####")
    print("1. pregunta01")
    print("2. pregunta02")
    print("3. pregunta03")
    print("4. Finalizado")
    opc=libreria.pedir_numero("ingrese una opcion:", 1, 4)
    #mapeo de las opciones
    if (opc == 1):
        incapaz()
    if (opc == 2):
        profesor()
    if (opc == 3):
        opinion()
print("¡Gracias!")
