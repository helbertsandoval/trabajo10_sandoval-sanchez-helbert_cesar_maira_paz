import libreria
#1.implementacion del sub menu
def ceviche_mixto():
    contenido=(input("¿Ingrese la cantidad de ceviche mixto?:"))+ "\n"
    libreria.guardar_datos("caliente.txt", contenido, "a")
    print("el costo del ceviche mixto es:", contenido*15)

def ceviche_pota():
    contenido=(input("Ingrese la cantidad de ceviche")) + "\n"
    libreria.guardar_datos("caliente.txt", contenido, "a")
    print("el costo del ceviche de pota es:", contenido*10)

def sudado():
    contenido=(input("Ingrese la cantidad de sudado")) + "\n"
    libreria.guardar_datos(("cabrilla.txt", contenido, "a"))
    print("el costo del sudado es:",contenido*12)
#menu de comandos
opc=0

max=3
while(opc != max):
    print("##### CABRILLA Y MAS ####")
    print("1. Ceviche mixto")
    print("2. Ceviche de pota")
    print("3. Sudado(pescado a escoger)")
    print("3. Finalizado")
    opc=libreria.pedir_numero("ingrese una opcion:", 1, 3)
    #mapeo de las opciones
    if (opc == 1):
        ceviche_mixto()
    if (opc == 2):
        ceviche_pota()
    if (opc == 3):
        sudado()

print("gracias por su compra ")
