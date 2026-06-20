from src.Logica.helpers.helpers import borrarPantalla as bp
import src.Logica.ingreso as ingreso
from src.Logica.opcionesUsuarios import *
from colorama import init, Fore, Style

init(autoreset=True)

menu:list=[]
opcion:int=0

def menuPrincipal(role:str="",nombre:str=""):
    """Función que muestra el menú principal del sistema. Permite a los usuarios seleccionar diferentes opciones para gestionar pedidos y usuarios, dependiendo de su rol (Admin o Usuario). Redirige a las funciones correspondientes según la opción seleccionada por el usuario.
     - Opción 1: Agregar pedido. Redirige a la función 'agregarPedido' para agregar un nuevo pedido al sistema.
     - Opción 2: Buscar pedido. Redirige a la función 'buscarPedido' para buscar un pedido existente en el sistema.
     - Opción 3: Ver pedidos. Redirige a la función 'verPedidos' para mostrar la lista de pedidos registrados en el sistema.
     - Opción 4: Modificar pedido. Redirige a la función 'modificarPedido' para modificar los datos de un pedido existente en el sistema.
     - Opción 5: Eliminar pedido. Redirige a la función 'eliminarPedido' para eliminar un pedido existente en el sistema.
     - Opción 6: Gestión de usuarios (solo para Admin). Redirige a la función 'subMenu' para mostrar el submenú de gestión de usuarios.
     - Opción 7: Salir. Redirige a la función 'ingreso' para volver al proceso de ingreso al sistema.
     - Opción no válida: Si el usuario selecciona una opción que no está en el menú, muestra un mensaje indicando que la opción no es válida y vuelve a mostrar el menú principal."""

    global opcion
    try:
        while opcion != "7":
            bp()    
            menu=[Fore.GREEN + Style.BRIGHT + f"Bienvenid@s al menú principal {nombre}" + Style.RESET_ALL,"\n1.-Agregar pedido\n2.-Buscar pedido\n3.-Ver pedidos\n4.-Modificar pedido\n5.-Eliminar pedido"]
            if role == "Admin":
                menu += [f"6.-Gestión de usuarios {role}","7.-Salir"]
            else:
                menu += ["7.-Salir"]

            for m in menu:
                print(m)

            opcion=input(Fore.GREEN + Style.BRIGHT + "\nIndique opción: " + Style.RESET_ALL).strip()

            match opcion:
                case "1":
                    print("Menú agregar pedidos")
                case "2":
                    print("Menú buscar pedidos")
                case "3":
                    print("Menú ver pedidos")
                case "4":
                    print("Menú modificar pedidos")
                case "5":
                    print("Menú eliminar pedidos")
                case "6":
                    if role == "Admin":
                        from src.Logica.submenu import subMenu as submenu
                        submenu()
                    else:
                        print(Fore.RED + Style.BRIGHT + "\nUsted no es un administrador." + Style.RESET_ALL)
                        time.sleep(2)
                        continue
                case "7":
                    print(Fore.RED + Style.BRIGHT + "\nSaliendo . . ." + Style.RESET_ALL)
                    time.sleep(2)
                    ingreso.ingreso()
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

    return opcion