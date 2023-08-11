from src.models.repositories.products_repository import products_repository


class ProductController:

    def register_product(self, product):
        try:
            products_repository.register_product(product)
            return "Produto Cadastrado Com Sucesso!"
        except:
            return "Erro ao Cadastrar Produto!"

    def list_products(self):
        products = products_repository.get_products()

        for product in products:
            return product
        
    def remove_product(self, product_name:str):
        products = products_repository.get_products()

        for product in products:
            try:
                if product['name'].lower() == product_name.lower():
                    products_repository.delete_product(product_name)
                    return f" O produto: {product['name']} foi removido com sucesso!"
                return "Produto Inexistente!"
            except:
                return "Impossível Remover produto"

