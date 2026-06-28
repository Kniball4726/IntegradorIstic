from src.Logica.helpers.helpers import borrarPantalla as bp
from src.Logica.menu import menuPrincipal as menu
from src.Persistencia.datos.estructuras import usuarios
import time
from colorama import init, Fore, Style
init(autoreset=True)

dni:int=0
user:str=""
password:str=""
usuarios:dict=usuarios

def ingreso():

    """
    Función que maneja el proceso de ingreso al sistema. Solicita al usuario que ingrese su DNI, nombre de usuario y contraseña. Verifica si el DNI está registrado en el sistema y si las credenciales son correctas. Si el ingreso es exitoso, redirige al menú principal según el rol del usuario (Admin o Usuario). Si el ingreso falla, muestra mensajes de error y vuelve a solicitar los datos de ingreso.
     - Si el DNI no está registrado, muestra un mensaje indicando que el DNI no se encuentra registrado y vuelve a solicitar los datos de ingreso.
     - Si el usuario o la contraseña son incorrectos, muestra un mensaje indicando que el usuario o la contraseña son incorrectos y vuelve a solicitar los datos de ingreso.
     - Si el usuario interrumpe el proceso de ingreso (por ejemplo, presionando Ctrl+C), muestra un mensaje indicando que se está saliendo del sistema y termina la ejecución del programa.
     - Si el usuario ingresa un valor no numérico para el DNI, muestra un mensaje indicando que se debe indicar un número válido y vuelve a solicitar los datos de ingreso.
     - Si el usuario ingresa un valor no numérico para el DNI, muestra un mensaje indicando que se debe indicar un número válido y vuelve a solicitar los datos de ingreso.  

    """
    
    global dni, password, user, usuarios
    
    try:
        while True:
            bp()
            print(Fore.GREEN + Style.BRIGHT + "Bienvenido al sistema de pedidos mayoristas.\nDebe indicar sus datos para ingresar\n\n" + Style.RESET_ALL)
            print(Fore.RED+"Para salir coloque DNI 1")
            dni=int(input("\nIndique su DNI: "))
            
            if dni in usuarios: 
                user=input("\nIndique su usuario: ").capitalize()
                password=input("\nIndique su contraseña: ")
                if user == usuarios[dni]["user"] and usuarios[dni]["password"] == password:
                    role = usuarios[dni]["role"]
                    menu(role, user)
                elif user != usuarios[dni]["user"] and usuarios[dni]["password"] == password:
                    print(Fore.RED + Style.BRIGHT + "\nUsuario incorrecto" + Style.RESET_ALL)
                    time.sleep(2)
                    continue
                elif user == usuarios[dni]["user"] and usuarios[dni]["password"] != password:
                    print(Fore.RED + Style.BRIGHT + "\nContraseña incorrecta" + Style.RESET_ALL)
                    time.sleep(2)
                    continue
                else:
                    print(Fore.RED + Style.BRIGHT + "\nUsuario y contraseña incorrecto" + Style.RESET_ALL)
                    time.sleep(2)
                    continue
            elif dni == 1:
                print(Fore.RED +"\nSaliendo . . .")
                time.sleep(2)
                return False
            else:
                print(Fore.RED + Style.BRIGHT + "\nEl DNI no se encuentra registrado" + Style.RESET_ALL)
                time.sleep(2)
                continue

    except ValueError:
        print(Fore.RED + Style.BRIGHT + "\nIndique un número valido" + Style.RESET_ALL)
        time.sleep(2)
        ingreso()
    except TypeError:
        print(Fore.RED + Style.BRIGHT + "\nIndique un número valido" + Style.RESET_ALL)
        time.sleep(2)
        ingreso()
    except KeyboardInterrupt:
        print(Fore.RED + Style.BRIGHT + "\nSaliendo . . ." + Style.RESET_ALL)
        time.sleep(2)
        exit()