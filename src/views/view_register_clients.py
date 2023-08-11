def view_register_client():
    name = input("Digite o nome do Cliente: ")
    phone = input("Digite o Telefone: ")
    state = input("Digite o Estado: ")

    return {"name": name, "phone": phone, "state": state}

def client_response(reponse):
    print("Response")