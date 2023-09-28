from Usuario import Usuario


class Cliente(Usuario):

  def __init__(self, email, contrasenia):
    super().__init__(email, contrasenia)
    self.tipoUsuario = "Cli"

  def menu(self):
    bucle = 0
    opcion = 0
    print("Bienvenido Cliente: ", self.email)
    while bucle != 1:
      try:
        #1- Realizar peticiond e un proyecto.
        #2- Podra realizar la compra
        #3- salir
        opcion = int(input("1-Peticion Proyecto, 2-Compra, 3-Salir"))
      except ValueError:
        print("Se ingreso mal")
      if opcion == 1:
        self.menuProyecto()
      elif opcion == 2:
        self.menuCompra()
      elif opcion == 3:
        print("Salir")
        bucle = 1
      elif opcion < 1 or opcion > 3:
        print("Opcion incorrecta, vuelva a ingresar una opcion entre 1 y 3")

  def menuProyecto(self):
    print("Panel de peticion de proyecto")

  def menuCompra(self):
    print("Panel de compra del libro")
