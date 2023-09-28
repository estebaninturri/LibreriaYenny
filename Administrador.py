from Usuario import Usuario


class Administrador(Usuario):

  def __init__(self, email, contrasenia):
    super().__init__(email, contrasenia)
    self.tipoUsuario = "Adm"

  def menu(self):
    bucle = 0
    opcion = 0
    print("Bienvenido Administrador: ", self.email)
    while bucle != 1:
      try:
        #1- panel abm.
        #2- podra hacer el seguimiento de las peticiones de los clientes, aprobarlos y rechazarlos
        #3- estadisticas de ventas
        #4- estadisticas de los proyectos
        #5- salir
        opcion = int(
            input("1-ABM, 2-Peticiones Clte, 3-Est Vta, 4-Est Proy, 5-Salir"))
      except ValueError:
        opcion = 0
      if opcion == 1:
        self.menuAbm()
      elif opcion == 2:
        print("Bienvenido al panel de peticiones de los clientes ")
      elif opcion == 3:
        print("Panel de estadisticas de las ventas mensual")
      elif opcion == 4:
        print("Panel de estadisticas del proyecto")
      elif opcion == 5:
        print("Salir")
        bucle = 1
      elif opcion < 1 or opcion > 5:
        print("Opcion no valida, ingrese de nuevo")

  def menuAbm(self):
    bucle = 0
    opcion = 0
    print("Bienvenido al panel ABM:")
    while bucle != 1:
      try:
        opcion = int(input("1-Usuario, 2-Libro, 3-Stock, 4-Sucursal, 5-Salir"))
      except ValueError:
        opcion = 0
        #print("Se ingreso mal")
      if opcion == 1:
        print("bienvenido al panel de usuario")
      elif opcion == 2:
        print("bienvenido al panel de libro")
      elif opcion == 3:
        print("bienvenido al panel de stock")
      elif opcion == 4:
        print("bienvenido al panel de sucursal")
      elif opcion == 5:
        print("Salir")
        bucle = 1
      elif opcion < 1 or opcion > 5:
        print("Opcion no valida, ingrese de nuevo")
