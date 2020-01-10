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
