from src.Logica.helpers.helpers import borrarPantalla as bp
from src.Persistencia.Usuarios import *

pedidos:list=[]

def agregarUsuario():
    bp()
    user=input("Indique usuario: ")
    password=input("Indique contraseña: ")
    role=input("Indique rol: ")

    usuario = Usuarios(user, password, role)




def agregarPedido():
    bp()
    print("Menú agregar pedidos")