from src.controllers.clients.clients_controller import ClientsController
from src.views.view_select_state_client import (
    view_select_state_client,
    view_clients_by_state,
)


def list_clients_by_state_constructor():
    clients_controller = ClientsController()
    state = view_select_state_client().lower()
    response = clients_controller.filter_client_by_state(state)
    view_clients_by_state(response)
