from .menu import menuPrincipal
from .helpers.helpers import borrarPantalla as bp
from .opcionesUsuarios import agregarUsuario, buscarUsuario, verUsuarios, modificarUsuario, eliminarUsuario
import time
from colorama import init, Fore, Style

init(autoreset=True)

opcion:str=""
submenu:list=[]

def subMenu(dni:int=0):
    """
    Función que muestra el submenú de gestión de usuarios para los administradores. Permite agregar, buscar, ver, modificar y eliminar usuarios, así como volver al menú principal. Redirige a las funciones correspondientes según la opción seleccionada por el usuario.
     - Opción 1: Agregar usuario. Redirige a la función 'agregarUsuario' para agregar un nuevo usuario al sistema.
     - Opción 2: Buscar usuario. Redirige a la función 'buscarUsuario' para buscar un usuario existente en el sistema.
     - Opción 3: Ver usuarios. Redirige a la función 'verUsuarios' para mostrar la lista de usuarios registrados en el sistema.
     - Opción 4: Modificar usuario. Redirige a la función 'modificarUsuario' para modificar los datos de un usuario existente en el sistema.
     - Opción 5: Eliminar usuario. Redirige a la función 'eliminarUsuario' para eliminar un usuario existente en el sistema.
     - Opción 6: Volver al menú principal. Redirige a la función 'menuPrincipal' para volver al menú principal del sistema.
     - Opción no válida: Si el usuario selecciona una opción que no está en el submenú, muestra un mensaje indicando que la opción no es válida y vuelve a mostrar el submenú.
    """
    global opcion,submenu
    opcion = ""  # Resetear para que el while funcione correctamente
    try:
        while opcion != "6":
            bp()
        
            print(Fore.GREEN + Style.BRIGHT + "Menú gestión de usuarios\n" + Style.RESET_ALL)

            submenu=["1.-Agregar usuario","2.-Buscar usuario","3.-Ver usuarios","4.-Modificar usuario","5.-Eliminar usuario","6.-Volver al menú principal"]
            for s in submenu:
                print(s)

            opcion=input(Fore.GREEN + Style.BRIGHT + "\nIndique opción: " + Style.RESET_ALL).strip()

            match opcion:
                case "1":
                    agregarUsuario()
                case "2":
                    buscarUsuario()
                case "3":
                    verUsuarios()
                case "4":
                    modificarUsuario()
                case "5":
                    eliminarUsuario()
                case "6":
                    print(Fore.RED + Style.BRIGHT + "\nVolviendo al menú principal . . ." + Style.RESET_ALL)
                    time.sleep(2)
                    menuPrincipal("Admin")
                case _:
                    print(Fore.RED + Style.BRIGHT + "\nOpción no válida" + Style.RESET_ALL)
                    time.sleep(2)
                    continue
    except ValueError:
        print(Fore.RED + Style.BRIGHT + "\nOpción no válida, debe indicar un número" + Style.RESET_ALL)
        time.sleep(2)
        subMenu()
    except KeyboardInterrupt:
        print(Fore.RED + Style.BRIGHT + "\nSaliendo . . ." + Style.RESET_ALL)
        time.sleep(2)
        exit()
    except TypeError:
        print(Fore.RED + Style.BRIGHT + "\nOpción no válida, debe indicar un número" + Style.RESET_ALL)
        time.sleep(2)
        subMenu()
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f"\nOcurrió un error: {e}" + Style.RESET_ALL)
        time.sleep(2)
        subMenu()