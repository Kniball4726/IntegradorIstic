from src.Logica.helpers.helpers import borrarPantalla as bp
from src.Logica.opciones import *
from src.Logica.submenu import subMenu as submenu
import colorama
from colorama import init, Fore, Style

init(autoreset=True)

"""
    Este módulo se encarga de mostrar el menú principal y redirigir a las funciones correspondientes según la opción seleccionada por el usuario. El menú se adapta según el rol del usuario (Admin o Usuario), mostrando opciones adicionales para los administradores. Las funciones para cada opción se encuentran en el módulo 'opciones'.

"""

menu:list=[]
opcion:int=0

def menuPrincipal(role:str=""):
    """Función que muestra el menú principal y redirige a las funciones correspondientes según la opción seleccionada por el usuario. El menú se adapta según el rol del usuario (Admin o Usuario)."""
    
    global opcion
    try:
        while opcion != 7:
            bp()    
            menu=[Fore.GREEN + Style.BRIGHT + "Bienvenid@s al menú principal" + Style.RESET_ALL,"\n1.-Agregar pedido\n2.-Buscar pedido\n3.-Ver pedidos\n4.-Modificar pedido\n5.-Eliminar pedido"]
            if role == "Admin":
                menu += ["6.-Gestión de usuarios","7.-Salir"]
            else:
                menu += ["7.-Salir"]

            for m in menu:
                print(m)
            opcion=int(input(Fore.GREEN + Style.BRIGHT + "\nIndique opción: " + Style.RESET_ALL))

            match opcion:
                case 1:
                    agregarPedido()
                case 2:
                    print("Menú buscar pedidos")
                case 3:
                    print("Menú ver pedidos")
                case 4:
                    print("Menú modificar pedidos")
                case 5:
                    print("Menú eliminar pedidos")
                case 6:
                    if role == "Admin":
                        submenu()
                    else:
                        print(Fore.RED + Style.BRIGHT + "\nUsted no es un administrador." + Style.RESET_ALL)
                        time.sleep(2)
                        continue
                case 7:
                    print(Fore.RED + Style.BRIGHT + "\nSaliendo . . ." + Style.RESET_ALL)
                    time.sleep(2)
                    exit()
                case _:
                    print(Fore.RED + Style.BRIGHT + "\nOpción no válida" + Style.RESET_ALL)
                    time.sleep(2)
                    continue
    except ValueError:
        print(Fore.RED + Style.BRIGHT + "\nOpción no válida, debe indicar un número" + Style.RESET_ALL)
        time.sleep(2)
        menuPrincipal(role)
    except KeyboardInterrupt:
        print(Fore.RED + Style.BRIGHT + "\nSaliendo . . ." + Style.RESET_ALL)
        time.sleep(2)
        exit()
    except TypeError:
        print(Fore.RED + Style.BRIGHT + "\nOpción no válida, debe indicar un número" + Style.RESET_ALL)
        time.sleep(2)
        menuPrincipal(role)
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f"\nOcurrió un error: {e}" + Style.RESET_ALL)
        time.sleep(2)
        menuPrincipal(role)
     