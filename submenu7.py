import libreria
#1. Implementacion de submenu
def agregarCostototal():
    #1 agregamos el costo fijo
    #2 agregamos el costo variable
    #3 hallamos el costo total
    costo_fijo=libreria.pedir_numero("ingrese costo fijo",3,30)
    costo_variable=libreria.pedir_numero("ingrese costo variable",2,50)
    print("ingrese el costo total", costo_fijo+costo_variable)
def agregarCostofijo():
    #1 agregar el costo total
    #2 agregar el costo variable
    #3 calcular el costo fijo
    costo_total=libreria.pedir_numero("ingrese costo total",60,120)
    costo_variable=libreria.pedir_numero("ingrese costo variable",2,45)
    print("ingrese el costo fijo ",costo_total-costo_variable )
# Menu de comandos
opc=0
max=3
while(opc!= max):
    print("############### MENU ##############")
    print("#1. agregar costo total")
    print("#2. agregar costo fijo")
    print("#3. Salir ")
    #2. Eleccion de la opcion menu
    opc=libreria.pedir_numero("Ingreso la opcion:", 1, 3)
    #3. Mapeo de las opciones
    if (opc==1):
        agregarCostototal()
    if (opc==2):
        agregarCostofijo()
