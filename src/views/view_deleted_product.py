def view_product_to_delete():
    name = input("Digite o Nome do produto que deseja deletar: ").lower()
    flavor = input("Digite o Sabor do produto que deseja deletar: ").lower()
    return {"name": name, "flavor": flavor}


def view_product_deleted(response):
    print(response)
