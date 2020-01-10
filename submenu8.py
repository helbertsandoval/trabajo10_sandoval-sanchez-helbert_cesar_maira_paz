import libreria
#1. Implementacion de submenu
def agregarCostofijomedio():
    #1 agregar el costo fijo
    #2 agregamos la produccion
    #3 hallamos el costo fijo medio
    costo_fijo=libreria.pedir_numero("ingrese costo fijo",110,240)
    produccion=libreria.pedir_numero("ingrese costo variable",2,80)
    print("ingrese el costo fijo medio", costo_fijo/produccion)

def agregarProduccion():
    #1 agregar el costo fijo
    #2 agregamos el costo fijo medio
    #3 calculamos la produccion
    costo_fijo=libreria.pedir_numero("ingrese costo fijo medio",45,90)
    costo_fijo_medio=libreria.pedir_numero("ingrese costo fijo medio",2,15)
    print("ingrese la produccion",costo_fijo/costo_fijo_medio)
# Menu de comandos
opc=0
max=3
while(opc!= max):
    print("############### MENU ##############")
    print("#1. agregar costo fijo medio")
    print("#2. agreegar produccion")
    print("#3. Salir ")
    #2. Eleccion de la opcion menu
    opc=libreria.pedir_numero("Ingreso la opcion:", 1, 3)
    #3. Mapeo de las opciones
    if (opc==1):
        agregarCostofijomedio()
    if (opc==2):
        agregarProduccion()
