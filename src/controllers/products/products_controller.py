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
        if not products:
            return "Não há produtos cadastrados"
        
        return products
    
    def remove_product(self, product_name: str):
            try:
                response = products_repository.delete_product(product_name)
                if not response:
                    return "Produto inexistente"
                return response
                
            except ValueError as err:
                print(err)
