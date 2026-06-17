import time
import colorama
from colorama import init, Fore, Style
init(autoreset=True)

from src.Logica.helpers.helpers import borrarPantalla as bp
from src.Persistencia.Usuarios import *

pedidos:dict={}
usuarios:dict={}

def agregarUsuario():
    """Función que permite agregar un nuevo usuario al sistema. Solicita al usuario que ingrese su nombre de usuario, contraseña y rol (Admin o Usuario). Luego, crea una instancia de la clase Usuarios con los datos ingresados y la agrega a la lista de usuarios."""
    global usuarios
    bp()
    dni=int(input("Indique DNI: "))
    user=input("Indique usuario: ").capitalize()
    password=input("Indique contraseña: ")
    role=input("Indique rol: ").capitalize()
    if role != "Admin" and role != "User":
        print(Fore.RED + Style.BRIGHT + "\nRol no válido, se asignará el rol de Usuario por defecto" + Style.RESET_ALL)
        role = "User"
    else:
        usuarios[dni] = {
            "user": user,
            "password": password,
            "role": role
        }


    usuario = Usuarios(user, password, role)
    usuarios[dni] = usuario

    print(Fore.GREEN + Style.BRIGHT + "\nUsuario agregado exitosamente" + Style.RESET_ALL)
    time.sleep(2)
    print(usuarios)



def agregarPedido():
    """Función que permite agregar un nuevo pedido al sistema. Solicita al usuario que ingrese los detalles del pedido y luego lo agrega a la lista de pedidos."""
    bp()
    print("Menú agregar pedidos")