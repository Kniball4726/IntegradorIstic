class Usuarios:
    """Clase que representa a un usuario del sistema. Contiene atributos como el nombre de usuario, contraseña y rol (Admin o Usuario). También incluye métodos para obtener y establecer estos atributos, así como un método para mostrar toda la información del usuario.
    """
    def __init__(self, user, password, role):
        self.user=user
        self.password=password
        self.role=role


    def getUser(self):
        return self.user
    
    def getPassword(self):
        return self.password
    
    def getRole(self):
        return self.role
    
    def setUser(self, user):
        self.user = user
    
    def setPassword(self, password):
        self.password = password
    
    def setRole(self, role):
        self.role = role
    
    def getTodo(self):
        return f"Nombre: {self.user}\nPassword: {self.password}\nRole: {self.role}"
    
    