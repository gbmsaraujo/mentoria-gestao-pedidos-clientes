class __ClientsRepository:
    def __init__(self):
        self.clients = []
    
    def register_clients(self, client):
        self.clients.append(client)
    
    def get_clients(self):
        return self.clients
    

clients_repository = __ClientsRepository()