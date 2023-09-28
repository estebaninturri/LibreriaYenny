from Usuario import Usuario

class Vendedor(Usuario):
  def __init__(self,email, contrasenia):
    super().__init__(email, contrasenia)
    self.tipoUsuario="Cli"
  def menu(self):
    bucle = 0
    opcion = 0
    print("Bienvenido Vendedor: ", self.email)
    while bucle != 1:
      try:
        #1- actualizar stock.
        #2- seguimiento de los proyectos de los cliente
        #3- estadisticas de ventas
        #4- hacer el cierre de caja de su respectiva sucursal
        #5- salir
        opcion = int(input("1-Act Stock,2- Sgmto Proy,3-Est Vta,4-Cierre Caja,5-Salir"))
      except ValueError:
        print("Se ingreso mal")
      if opcion == 1:
        self.menuStock()
      elif opcion == 2:
        print("Aca estaria el seguimiento de las peticiones del cliente")
      elif opcion == 3:
        print("Panel de estadisticas de las ventas mensual")
      elif opcion == 4:
        self.cierreCaja()
      elif opcion == 5:
        print("Salir")
        bucle = 1

  def menuStock(self):
    print("Panel de actualizacion de stock")

  def cierreCaja(self):
    print("¿Confirma hacer el cierre de caja?")
    opcCierre=""
    while (opcCierre !="si" and opcCierre!="no"):
      try:
        #1- actualizar stock.
        #2- seguimiento de los proyectos de los cliente
        #3- estadisticas de ventas
        #4- hacer el cierre de caja de su respectiva sucursal
        #5- salir
        opcCierre = str(input("Ingrese si / no"))
        opcCierre=opcCierre.lower()
        if(opcCierre=="si"):
          print("Cierre de caja realizado")
        elif(opcCierre=="no"):
          print("Cierre de caja cancelado")
        else:
          print("Opcion incorrecta")
      except ValueError:
        opcCierre=""
        print("Se ingreso mal")