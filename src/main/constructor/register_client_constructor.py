from src.controllers.clients.clients_controller import ClientsController
from src.views.view_register_clients import view_register_client, client_response


def register_client_constructor():
    clients_controller = ClientsController()

    clients = view_register_client()

    response = clients_controller.register_client(clients)

    client_response(response)
