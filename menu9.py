import libreria
# Menu de comandos
opc=0
max=3
while(opc!= max):
    print("############### MENU ##############")
    print("#1. agregar costo variable medio")
    print("#2. agreegar costo variable")
    print("#3. Salir ")
    #2. Eleccion de la opcion menu
    opc=libreria.pedir_numero("Ingreso la opcion:", 1, 3)
    #3. Mapeo de las opciones
    if (opc==1):
        agregarCostovariablemedio()
    if (opc==2):
        agregarCostovariable()
