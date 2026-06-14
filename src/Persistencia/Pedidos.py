class Pedidos:
    """Clase que representa un pedido realizado por un cliente. Contiene atributos como el ID del pedido, DNI del cliente, producto solicitado, cantidad y estado del pedido. También incluye un método para mostrar toda la información del pedido.
    """
    def __init__(self, idPedido, dniCliente, producto, cantidad, estado):
        self.idPedido = idPedido
        self.dniCliente = dniCliente
        self.producto = producto
        self.cantidad = cantidad
        self.estado = estado

    def __str__(self):
        return f"ID Pedido: {self.idPedido}, DNI Cliente: {self.dniCliente}, Producto: {self.producto}, Cantidad: {self.cantidad}, Estado: {self.estado}"
