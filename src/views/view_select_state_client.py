def view_select_state_client():
    return input("Por qual estado deseja fazer a busca? ")

def view_clients_by_state(clients):
    for client in clients:
        print(f"* {client['name']}")
