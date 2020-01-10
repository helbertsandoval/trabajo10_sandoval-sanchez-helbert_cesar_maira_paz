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
