import time
from ..Persistencia.datos.estructuras import pedidos as pedidos
from .helpers.helpers import borrarPantalla as bp
from colorama import init, Fore, Style
init(autoreset=True)

def buscarPedido():
    remito:int=0

    try:
        bp()
        print(Fore.GREEN+"Buscar Pedido")
        remito=int(input("\nIndique remito a buscar: "))
        
        if remito in pedidos.keys():
            bp()
            print(Fore.GREEN + f"✓ Pedido Encontrado")
            print(Fore.GREEN+f"\n{'='*50}")
            print(Fore.GREEN+f"Pedido {remito}:")
            print(Fore.GREEN+f"{'='*50}")
            print(f"Cliente: {pedidos[remito]['cliente']}")
            print(f"Bultos: {pedidos[remito]['bultos']}")
            print(f"Logística: {pedidos[remito]['logistica']}")
            print(f"Operario: {pedidos[remito]['operario']}")
            print(f"\nProductos:")
            for prod in pedidos[remito]['productos']:
                print(f"  - {prod['producto']}: {prod['cantidad']} unidades")
            print()
            input(Fore.RED+"\nPresione para continuar . . .")
            return True
        else:
            bp()
            print(Fore.RED + "\n✗ Pedido no encontrado")
            time.sleep(2)
            return False

    except TypeError:
        print("\nError en el tipo de datos")
        time.sleep(2)
        buscarPedido()
    except ValueError:
        print(Fore.RED+"\nIndique un número valido")
        time.sleep(2)
        buscarPedido()
    except KeyboardInterrupt:
        print(Fore.RED + "\nSaliendo . . .")
        time.sleep(2)
        exit()


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
            print(Fore.GREEN + f"Producto {numeros+1} de {cantprod}\n")
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

        bp()
        print(Fore.GREEN + f"✓ Pedido Registrado")
        print(Fore.GREEN+f"\n{'='*50}")
        print(Fore.GREEN+f"Pedido {remito}:")
        print(Fore.GREEN+f"{'='*50}")
        print(f"Cliente: {pedidos[remito]['cliente']}")
        print(f"Bultos: {pedidos[remito]['bultos']}")
        print(f"Logística: {pedidos[remito]['logistica']}")
        print(f"Operario: {pedidos[remito]['operario']}")
        print(f"\nProductos:")
        for prod in pedidos[remito]['productos']:
            print(f"  - {prod['producto']}: {prod['cantidad']} unidades")
        print()

        input(Fore.RED+"\nPresione para continuar")
    except TypeError:
        print("\nError en el tipo de datos")
        time.sleep(2)
        agregarPedido()
    except ValueError:
        print("\nIndique un número valido")
        time.sleep(2)
        agregarPedido()
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
        for remito, datos in pedidos.items():
            print(Fore.GREEN+f"\n{'='*50}")
            print(Fore.GREEN+f"Pedido {remito}:")
            print(Fore.GREEN+f"{'='*50}")
            print(f"Cliente: {datos['cliente']}")
            print(f"Bultos: {datos['bultos']}")
            print(f"Logística: {datos['logistica']}")
            print(f"Operario: {datos['operario']}")
            print(f"Productos:")
            for prod in datos['productos']:
                print(f"  - {prod['producto']}: {prod['cantidad']} unidades")
            print()
    else:
        print(Fore.RED+"No se encontraron registros")
    input(Fore.RED+"\nPresione una tecla para volver . . .")

def modificarPedido():
    global pedidos
    remito: int = 0
    
    try:
        bp()
        print(Fore.GREEN+"Modificar Pedido")
        remito = int(input("\nIndique remito a modificar: "))
        
        if remito in pedidos.keys():
            # Mostrar datos actuales
            bp()
            print(Fore.GREEN+f"\n{'='*50}")
            print(Fore.GREEN+f"Pedido {remito}:")
            print(Fore.GREEN+f"{'='*50}")
            print(f"Cliente: {pedidos[remito]['cliente']}")
            print(f"Bultos: {pedidos[remito]['bultos']}")
            print(f"Logística: {pedidos[remito]['logistica']}")
            print(f"Operario: {pedidos[remito]['operario']}")
            print(f"\nProductos:")
            for prod in pedidos[remito]['productos']:
                print(f"  - {prod['producto']}: {prod['cantidad']} unidades")
            print()
            
            # Menú de modificación
            print(Fore.YELLOW + "\n¿Qué desea modificar?")
            print("1. Cliente")
            print("2. Bultos")
            print("3. Logística")
            print("4. Operario")
            print("5. Productos")
            print("0. Cancelar")
            
            opcion = input("\nSeleccione opción: ")
            
            if opcion == "1":
                pedidos[remito]['cliente'] = input("Nuevo cliente: ").strip()
                print(Fore.GREEN+"\nCliente modificado exitosamente")
            elif opcion == "2":
                pedidos[remito]['bultos'] = int(input("Nueva cantidad de bultos: "))
                print(Fore.GREEN+"\nBultos modificados exitosamente")
            elif opcion == "3":
                pedidos[remito]['logistica'] = input("Nueva logística: ")
                print(Fore.GREEN+"\nLogística modificada exitosamente")
            elif opcion == "4":
                pedidos[remito]['operario'] = input("Nuevo operario: ")
                print(Fore.GREEN+"\nOperario modificado exitosamente")
            elif opcion == "5":
                # Modificar productos
                cantprod = int(input("Cuantos articulos lleva el remito? "))
                productos_lista = []
                for numeros in range(cantprod):
                    bp()
                    print(Fore.GREEN + f"Producto {numeros+1} de {cantprod}\n")
                    productos=input("\nIndique nombre de producto: ")
                    cantidades=int(input("Indique cantidades: "))
                    prod = {"producto": productos, "cantidad": cantidades}
                    productos_lista.append(prod)
                pedidos[remito]['productos'] = productos_lista
                print(Fore.GREEN+"\nProductos modificados exitosamente")
            elif opcion != "0":
                print(Fore.RED+"Opción no válida")
                time.sleep(2)
                return
            else:
                print(Fore.YELLOW+"\nOperación cancelada")
                time.sleep(1)
                return
            
            input(Fore.RED+"\nPresione para continuar . . .")
        else:
            print(Fore.RED+"\nPedido no encontrado")
            time.sleep(2)
    
    except ValueError:
        print(Fore.RED+"\nIndique un número válido")
        time.sleep(2)
        modificarPedido()
    except KeyboardInterrupt:
        print(Fore.RED + "\nSaliendo . . .")
        time.sleep(2)
        exit()
    except Exception as e:
        print(f"\nOcurrió un error: {e}")
        time.sleep(2)
        modificarPedido()

def eliminarPedido():
    global pedidos
    remito: int = 0
    
    try:
        bp()
        print(Fore.GREEN+"Eliminar Pedido")
        remito = int(input("\nIndique remito a eliminar: "))
        
        if remito in pedidos.keys():
            # Mostrar datos del pedido a eliminar
            bp()
            print(Fore.RED+f"\n{'='*50}")
            print(Fore.RED+f"Pedido a Eliminar - Remito {remito}:")
            print(Fore.RED+f"{'='*50}")
            print(f"Cliente: {pedidos[remito]['cliente']}")
            print(f"Bultos: {pedidos[remito]['bultos']}")
            print(f"Logística: {pedidos[remito]['logistica']}")
            print(f"Operario: {pedidos[remito]['operario']}")
            print(f"\nProductos:")
            for prod in pedidos[remito]['productos']:
                print(f"  - {prod['producto']}: {prod['cantidad']} unidades")
            print()
            
            # Pedir confirmación
            print(Fore.RED + "\n¿Está seguro de que desea eliminar este pedido?")
            confirmacion = input("Escriba 'S' para confirmar o 'N' para cancelar: ").strip().upper()
            
            if confirmacion == "S":
                del pedidos[remito]
                print(Fore.GREEN+"\nPedido eliminado exitosamente")
                time.sleep(2)
            elif confirmacion == "N":
                print(Fore.YELLOW+"\nOperación cancelada")
                time.sleep(1)
            else:
                print(Fore.RED+"\nOpción no válida")
                time.sleep(2)
                return
            
            input(Fore.RED+"\nPresione para continuar . . .")
        else:
            print(Fore.RED+"\nPedido no encontrado")
            time.sleep(2)
    
    except ValueError:
        print(Fore.RED+"\nIndique un número válido")
        time.sleep(2)
        eliminarPedido()
    except KeyboardInterrupt:
        print(Fore.RED + "\nSaliendo . . .")
        time.sleep(2)
        exit()
    except Exception as e:
        print(f"\nOcurrió un error: {e}")
        time.sleep(2)
        eliminarPedido()
