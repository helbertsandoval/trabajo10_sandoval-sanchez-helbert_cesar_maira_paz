import libreria
#1. Implementacion de submenu
def agregarCostovariablemedio():
    #1 agregar coteo variable
    #2 agregar la produccion
    #3. calcular el costo variable medio
    costo_variable=libreria.pedir_numero("ingrese costo variable",50,800)
    produccion=libreria.pedir_numero("ingrese costo variable",2,40)
    print("ingresar el costo variable medio",costo_variable/produccion)
def agregarCostovariable():
    #1. agregar el costo variable medio
    #2 agregar la produccion
    #3 calcular el costo variable
    costo_variable_medio=libreria.pedir_numero("ingrese costo variable medio",40,70)
    produccion=libreria.pedir_numero("ingrese produccion",3,45)
    print("ingrese el costo variable",costo_variable_medio*produccion)
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
