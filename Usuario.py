class Usuario:

  def __init__(self, email, contrasenia):
    self.email = email
    self.contrasenia = contrasenia

  def crearSesion(self, email, contrasenia):
    if len(email) > 0 and len(contrasenia)>0:
      print("creaste la cuenta capooooo!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
      print("No se pudo guardar")
      
  def iniciarSesion(self,email, contrasenia):
    if len(email) > 0 and len(contrasenia)>0:
      print("iniciaste sesion mostro!!!!!!!!!")
    else:
      print("No se pudo iniciar:p")

  def cerrarSesion(self):
    print("cerraste sesion")