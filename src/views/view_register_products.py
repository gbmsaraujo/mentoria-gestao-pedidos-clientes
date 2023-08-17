def view_register_product():
    name = input("Digite o nome do produto: ").lower()
    flavor = input("Digite o sabor do produto: ").lower()
    return {"name": name, "flavor": flavor}

def response_products(response):
    print(response)