import time
from colorama import init, Fore, Style
init(autoreset=True)

from src.Logica.helpers.helpers import borrarPantalla as bp
from src.Persistencia.clases.Usuarios import *

pedidos:dict={}

def agregarUsuario():
    """Función que permite agregar un nuevo usuario al sistema. Solicita al usuario que ingrese su nombre de usuario, contraseña y rol (Admin o Usuario). Luego, crea una instancia de la clase Usuarios con los datos ingresados y la agrega a la lista de usuarios."""
    bp()
    import src.Logica.ingreso as ingreso
    print(Fore.GREEN + Style.BRIGHT + "Agregar nuevo usuario\n" + Style.RESET_ALL)
    dni=int(input("Indique DNI: "))
    user=input("Indique usuario: ").capitalize()
    password=input("Indique contraseña: ")
    role=input("Indique rol: ").capitalize()
    if role != "Admin" and role != "User":
        print(Fore.RED + Style.BRIGHT + "\nRol no válido, se asignará el rol de Usuario por defecto" + Style.RESET_ALL)
        role = "User"
    usuario = Usuarios(user, password, role)
    ingreso.usuarios[dni] = usuario

    print(Fore.GREEN + Style.BRIGHT + f"\nUsuario {user} agregado exitosamente" + Style.RESET_ALL)
    time.sleep(2)
    print(usuarios)


def verUsuarios():
    """Función que muestra la lista de usuarios registrados en el sistema. Recorre la lista de usuarios y muestra el DNI, nombre de usuario y rol de cada usuario registrado."""
    bp()
    import src.Logica.ingreso as ingreso
    print(Fore.GREEN + Style.BRIGHT + "Lista de usuarios registrados\n" + Style.RESET_ALL)
    for dni, usuario in ingreso.usuarios.items():
        print(f"DNI: {dni} - Usuario: {usuario.user} - Rol: {usuario.role}")
    input(Fore.GREEN + Style.BRIGHT + "\nPresione Enter para volver al submenú" + Style.RESET_ALL)

def eliminarUsuario():
    """Función que permite eliminar un usuario registrado en el sistema. Solicita al usuario que ingrese el DNI del usuario que desea eliminar. Verifica si el DNI está registrado en la lista de usuarios y, si es así, elimina el usuario correspondiente. Si el DNI no está registrado, muestra un mensaje indicando que el DNI no se encuentra registrado."""
    global usuarios
    bp()
    dni=int(input("Indique DNI del usuario a eliminar: "))
    if dni in usuarios:
        del usuarios[dni]
        print(Fore.GREEN + Style.BRIGHT + f"\nUsuario con DNI {dni} eliminado exitosamente" + Style.RESET_ALL)
    else:
        print(Fore.RED + Style.BRIGHT + "\nDNI no registrado" + Style.RESET_ALL)
    time.sleep(2)

