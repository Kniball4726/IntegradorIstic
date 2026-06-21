import time
from src.Persistencia.datos.estructuras import pedidos as pedidos
from src.Logica.helpers.helpers import borrarPantalla as bp
from colorama import init, Fore, Style
init(autoreset=True)

def buscarPedido():
    remito:int=0

    try:
        bp()
        print(Fore.GREEN+"Buscar Pedido")
        remito=int(input("\nIndique remito a buscar: "))
        return remito in pedidos[0].values()
    
    except TypeError:
        print("\nError en el tipo de datos")
        time.sleep(2)
        buscarPedido()
    except ValueError:
        print("\nIndique un número valido")
        time.sleep(2)
        buscarPedido()


def agregarPedido():
    remito:int=0
    cliente:str=""
    bultos:int=0
    logistica:str=""
    operario:str=""
    cantprod:int=0
    productos_lista:list=[]
    global pedidos

    try:    
        bp()
        print(Fore.GREEN+"Agregar Pedido")
        remito=int(input("\nIndique remito: "))
        cliente=input("Indique cliente: ").strip()
        bultos=int(input("Indique cantidad de bultos: "))
        logistica=input("Indique logistica: ")
        operario=input("Indique operario: ")
        cantprod=int(input("Cuantos articulos lleva el remito? "))
        productos_lista = []
       
        for numeros in range(cantprod):
            bp()
            productos=input("\nIndique nombre de producto: ")
            cantidades=int(input("Indique cantidades: "))
            prod = {"producto": productos, "cantidad": cantidades}
            productos_lista.append(prod)

        pedidos[remito]={
                "cliente":cliente,
                "bultos":bultos,
                "logistica":logistica,
                "operario":operario,
                "productos": productos_lista
        }

        print(pedidos)
        time.sleep(3)
    except TypeError:
        print("\nError en el tipo de datos")
        time.sleep(2)
        buscarPedido()
    except ValueError:
        print("\nIndique un número valido")
        time.sleep(2)
        buscarPedido()
    except KeyboardInterrupt:
        print(Fore.RED + "\nSaliendo . . .")
        time.sleep(2)
        exit()
    except Exception as e:
        print(f"\nOcurrió un error: {e}")
        time.sleep(2)
        agregarPedido()

def verPedidos():
    global pedidos
    bp()
    if pedidos:
        for m in pedidos.items():
            print(m)
    else:
        print(Fore.RED+"No se encontraron registros")
    input(Fore.RED+"\nPresione una tecla para volver . . .")