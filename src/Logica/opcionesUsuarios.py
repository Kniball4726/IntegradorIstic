import time
from colorama import init, Fore, Style
init(autoreset=True)

from src.Logica.helpers.helpers import borrarPantalla as bp
from src.Persistencia.datos.estructuras import usuarios as usuarios
from src.Persistencia.clases.Usuarios import Usuarios

def agregarUsuario():
    """Función que permite agregar un nuevo usuario al sistema."""
    dni:int=0
    user:str=""
    password:str=""
    role:str=""
    global usuarios
    
    try:
        bp()
        print(Fore.GREEN + Style.BRIGHT + "Agregar nuevo usuario" + Style.RESET_ALL)
        print(Fore.GREEN + f"{'='*50}" + Style.RESET_ALL)
        
        dni=int(input("\nIndique DNI: "))
        
        if dni in usuarios:
            print(Fore.RED + "\nEl DNI ya está registrado" + Style.RESET_ALL)
            time.sleep(2)
            return
        
        user=input("Indique usuario: ").capitalize()
        password=input("Indique contraseña: ")
        print("Roles disponibles: Admin, User")
        role=input("Indique rol (Admin/User): ").capitalize()
        
        if role != "Admin" and role != "User":
            print(Fore.RED + "\nRol no válido, se asignará el rol de Usuario por defecto" + Style.RESET_ALL)
            role = "User"
        
        usuarios[dni] = {
            "user": user,
            "password": password,
            "role": role
        }
        
        print(Fore.GREEN + f"\n{'='*50}")
        print(f"✓ Usuario registrado exitosamente")
        print(f"{'='*50}")
        print(f"DNI: {dni}")
        print(f"Usuario: {user}")
        print(f"Rol: {role}")
        print(Fore.RESET_ALL)
        
        time.sleep(2)
    
    except ValueError:
        print(Fore.RED + "Indique un número válido para el DNI" + Style.RESET_ALL)
        time.sleep(2)
        agregarUsuario()
    except Exception as e:
        print(Fore.RED + f"Ocurrió un error: {e}" + Style.RESET_ALL)
        time.sleep(2)

def buscarUsuario():
    """Función que busca un usuario por DNI y muestra sus datos."""
    try:
        bp()
        print(Fore.GREEN + "Buscar Usuario" + Style.RESET_ALL)
        print(Fore.GREEN + f"{'='*50}" + Style.RESET_ALL)
        
        dni = int(input("\nIndique DNI a buscar: "))
        
        if dni in usuarios:
            bp()
            print(Fore.GREEN + f"✓ Usuario Encontrado")
            print(Fore.GREEN + f"\n{'='*50}")
            print(Fore.GREEN + f"Datos del Usuario:")
            print(Fore.GREEN + f"{'='*50}")
            print(f"DNI: {dni}")
            print(f"Usuario: {usuarios[dni]['user']}")
            print(f"Contraseña: {usuarios[dni]['password']}")
            print(f"Rol: {usuarios[dni]['role']}")
            print()
        else:
            bp()
            print(Fore.RED + "\n✗ Usuario no encontrado")
        
        time.sleep(2)
    
    except ValueError:
        print(Fore.RED + "Indique un número válido para el DNI" + Style.RESET_ALL)
        time.sleep(2)
        buscarUsuario()
    except Exception as e:
        print(Fore.RED + f"Ocurrió un error: {e}" + Style.RESET_ALL)
        time.sleep(2)

def verUsuarios():
    """Función que muestra la lista de usuarios registrados en el sistema."""
    bp()
    print(Fore.GREEN + Style.BRIGHT + "Lista de usuarios registrados" + Style.RESET_ALL)
    print(Fore.GREEN + f"{'='*70}" + Style.RESET_ALL)
    
    if not usuarios:
        print(Fore.YELLOW + "No hay usuarios registrados." + Style.RESET_ALL)
    else:
        for dni, datos in usuarios.items():
            print(f"\nDNI: {dni}")
            print(f"  Usuario: {datos['user']}")
            print(f"  Rol: {datos['role']}")
            print(f"  {'─'*66}")
    
    input(Fore.GREEN + Style.BRIGHT + "\nPresione Enter para volver al submenú" + Style.RESET_ALL)

def modificarUsuario():
    """Función que permite modificar los datos de un usuario existente."""
    global usuarios
    
    try:
        bp()
        print(Fore.GREEN + "Modificar Usuario" + Style.RESET_ALL)
        print(Fore.GREEN + f"{'='*50}" + Style.RESET_ALL)
        
        dni = int(input("\nIndique DNI del usuario a modificar: "))
        
        if dni in usuarios:
            bp()
            print(Fore.GREEN + f"{'='*50}")
            print(f"Usuario Encontrado - DNI {dni}")
            print(f"{'='*50}")
            print(f"Usuario actual: {usuarios[dni]['user']}")
            print(f"Rol actual: {usuarios[dni]['role']}")
            
            print(Fore.YELLOW + "\n¿Qué desea modificar?")
            print("1. Usuario")
            print("2. Contraseña")
            print("3. Rol")
            print("0. Cancelar")
            
            opcion = input("\nSeleccione opción: ").strip()
            
            if opcion == "1":
                nuevo_user = input("Nuevo usuario: ").capitalize()
                usuarios[dni]['user'] = nuevo_user
                print(Fore.GREEN + "\nUsuario modificado exitosamente")
            
            elif opcion == "2":
                nueva_password = input("Nueva contraseña: ")
                usuarios[dni]['password'] = nueva_password
                print(Fore.GREEN + "\nContraseña modificada exitosamente")
            
            elif opcion == "3":
                print("Roles disponibles: Admin, User")
                nuevo_role = input("Nuevo rol (Admin/User): ").capitalize()
                if nuevo_role not in ["Admin", "User"]:
                    print(Fore.RED + "Rol no válido")
                    time.sleep(2)
                    return
                usuarios[dni]['role'] = nuevo_role
                print(Fore.GREEN + "\nRol modificado exitosamente")
            
            elif opcion == "0":
                print(Fore.YELLOW + "Operación cancelada")
            else:
                print(Fore.RED + "Opción no válida")
            
            time.sleep(2)
        else:
            print(Fore.RED + "\nDNI no registrado")
            time.sleep(2)
    
    except ValueError:
        print(Fore.RED + "Indique un número válido para el DNI" + Style.RESET_ALL)
        time.sleep(2)
        modificarUsuario()
    except Exception as e:
        print(Fore.RED + f"Ocurrió un error: {e}" + Style.RESET_ALL)
        time.sleep(2)

def eliminarUsuario():
    """Función que permite eliminar un usuario registrado en el sistema."""
    global usuarios
    
    try:
        bp()
        print(Fore.GREEN + "Eliminar Usuario" + Style.RESET_ALL)
        print(Fore.GREEN + f"{'='*50}" + Style.RESET_ALL)
        
        dni = int(input("\nIndique DNI del usuario a eliminar: "))
        
        if dni in usuarios:
            bp()
            print(Fore.RED + f"{'='*50}")
            print(f"Usuario a Eliminar - DNI {dni}")
            print(f"{'='*50}")
            print(f"Usuario: {usuarios[dni]['user']}")
            print(f"Rol: {usuarios[dni]['role']}")
            print()
            
            confirmacion = input(Fore.RED + "¿Está seguro? Escriba 'S' para confirmar: " + Style.RESET_ALL).strip().upper()
            
            if confirmacion == "S":
                del usuarios[dni]
                print(Fore.GREEN + f"\n✓ Usuario con DNI {dni} eliminado exitosamente" + Style.RESET_ALL)
            else:
                print(Fore.YELLOW + "\nOperación cancelada")
        else:
            print(Fore.RED + "\nDNI no registrado")
        
        time.sleep(2)
    
    except ValueError:
        print(Fore.RED + "Indique un número válido para el DNI" + Style.RESET_ALL)
        time.sleep(2)
        eliminarUsuario()
    except Exception as e:
        print(Fore.RED + f"Ocurrió un error: {e}" + Style.RESET_ALL)
        time.sleep(2)

