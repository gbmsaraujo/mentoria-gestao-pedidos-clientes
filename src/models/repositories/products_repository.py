class __ProductsRepository:
    def __init__(self):
        self.products = []
    
    def register_product(self, product):
        self.products.append(product)
    
    def delete_product(self, product:str):
        self.products.remove(product)
    
    def get_products(self):
        return self.products
        

products_repository = __ProductsRepository()