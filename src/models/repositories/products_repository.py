class __ProductsRepository:
    def __init__(self):
        self.products = []

    def register_product(self, product):
        self.products.append(product)

    def delete_product(self, product_to_delete: dict):
        for product in self.products:
            if (
                product["name"] == product_to_delete["name"]
                and product["flavor"] == product_to_delete["flavor"]
            ):
                try:
                    self.products.remove(product)
                    return "Produto Removido Com Sucesso"
                except:
                    return "Erro ao Remover Produto"

    def get_products(self):
        return self.products


products_repository = __ProductsRepository()
