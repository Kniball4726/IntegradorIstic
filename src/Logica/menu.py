from src.Logica.helpers.helpers import borrarPantalla as bp
from src.Logica.opciones import *

menu:list=[]
opcion:int=0

menu=["Bienvenid@s al menú principal","\n1.-Agregar pedido\n2.-Buscar pedido\n3.-Ver pedidos\n4.-Modificar pedido\n5.-Eliminar pedido"]



def menuPrincipal(role:str=""):
    bp()
    global menu, opcion
    if role == "Admin":
        menu += ["6.-Gestión de usuarios","7.-Salir"]
    else:
        menu += ["6.-Salir"]

    for m in menu:
        print(m)
    opcion=int(input("\nIndique opción: "))

    match opcion:
        case 1:
            agregarPedido()