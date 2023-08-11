def view_register_product():
    name = input("Digite o nome do produto: ")
    flavor = input("Digite o sabor do produto: ")
    return {"name": name, "flavor": flavor}

def response_products(response):
    print(response)