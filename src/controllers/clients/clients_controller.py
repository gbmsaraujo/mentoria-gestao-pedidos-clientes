from src.models.repositories.clients_repository import clients_repository


class ClientsController:
    def register_client(self, client):
        try:
            if not client["name"] or not client["phone"] or not client["state"]:
                return "Todos os Campos São Obrigatórios, Tente novamente!"
            clients_repository.register_clients(client)
            return "Cliente Cadastrado com Sucesso!"

        except ValueError as err:
            print(err)
            # return "Impossível Cadastrar Cliente!"

    def filter_client_by_state(self, state):
        clients = clients_repository.get_clients()
        clients_filtered = []

        if not clients:
            return 'Nenhum Cliente Cadastrado!'
        
        for client in clients:
            if client['state'] == state:
                clients_filtered.append(client['name'])

        return clients_filtered 


