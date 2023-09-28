from Usuario import Usuario
from Administrador import Administrador
from Cliente import Cliente
from Vendedor import Vendedor

def menuInicioSesion(mail, contrasenia):
  bucle = 0
  opcion = 0
  usuario=""
  while bucle != 1:
    try:
      opcion = int(input("Ingrese una opc 1-Adm, 2-Ven, 3-Cliente,4-Salir\n"))
    except ValueError:
      opcion=0
      
    if opcion == 1:
      usuario=Administrador(mail, contrasenia)
      bucle = 1
    elif opcion == 2:
      usuario=Vendedor(mail,contrasenia)
      bucle = 1
    elif opcion == 3:
      usuario=Cliente(mail,contrasenia)
      bucle = 1
    elif opcion == 4:
      print("Salir")
      bucle = 1
    elif opcion < 1 or opcion >4:
      print("Opcion no valida, ingrese de nuevo")
      
  return usuario

bucle = 0
opcion = 0
while bucle != 1:
  try:
    opcion = int(
        input("Ingrese una opc 1-Iniciar Sesion, 2-Crear Sesion, 3-Salir\n"))
  except ValueError:
    print("Se ingreso mal")
  if opcion == 1:
    mail=input("Ingrese mail:\n")
    pwd=input("Ingrese la contraseña:\n")
    yo=menuInicioSesion(mail,pwd)
    if yo!="":
      yo.menu()
  elif opcion == 3:
    bucle = 1
print("Adiosss")