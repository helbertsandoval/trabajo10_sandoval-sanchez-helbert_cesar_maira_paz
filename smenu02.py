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
