import libreria
#1. Implementacion de submenu
def agregarAlumno():
    #1 agregar el nombre del alumno
   nombre=libreria.pedir_nombre("ingrese el nombre")
   print("nombre agregado")
def agregarEdad():
    #1 agregar la edad
    Edad=libreria.pedir_numero("ingrese la edad",1,80)
    print("edad agregado")

# Menu de comandos
opc=0
max=3
while(opc!= max):
    print("############### MENU ##############")
    print("#1. agregar nombre")
    print("#2. agregar edad ")
    print("#3. Salir ")
    #2. Eleccion de la opcion menu
    opc=libreria.pedir_numero("Ingreso la opcion:", 1, 3)
    #3. Mapeo de las opciones
    if (opc==1):
        agregarAlumno()
    if (opc==2):
        agregarEdad()

#fin_menu
