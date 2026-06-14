from src.Logica.helpers.helpers import borrarPantalla as bp
from src.Logica.menu import menuPrincipal as menu
import time

dni:int=0
user:str=""
password:str=""
usuarios:dict={}

usuarios={
    95777596:{
        "user":"Admin",
        "password":"admin123",
        "role":"Admin"
    },
    12345678:{
        "user":"Usuario",
        "password":"usuario123",
        "role":"User"
    }
}



def ingreso():

    """
        Programa de ingreso al sistema con datos hardcodeados
    """
    
    global dni, password, user, usuarios
    
    try:
        bp()
        print("Bienvenido al sistema de pedidos mayoristas.\nDebe indicar sus datos para ingresar\n\n")
        dni=int(input("Indique su DNI: "))
        
        if dni in usuarios: 
            user=input("\nIndique su usuario: ").capitalize()
            password=input("\nIndique su contraseña: ")
            if user == usuarios[dni]["user"] and usuarios[dni]["password"] == password:
                menu(usuarios[dni]["role"])
            else:
                print("\nUsuario o contraseña incorrecto") 
                ingreso()
        else:
            print("El DNI no se encuentra registrado")
            ingreso()
                
    except ValueError:
        print("\nIndique un número valido")
        time.sleep(2)
        ingreso()
    except TypeError:
        print("\nIndique un número valido")
        time.sleep(2)
        ingreso()
    except KeyboardInterrupt:
        print("\nSaliendo . . .")
        time.sleep(2)
        exit()
    