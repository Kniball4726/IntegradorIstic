class Usuarios:
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
    
    def getTodo(self):
        return f"Nombre: {self.user}\nPassword: {self.password}\nRole: {self.role}"
    
    