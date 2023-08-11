from src.controllers.products.products_controller import ProductController
from src.views.view_register_products import view_register_product, response_products


def register_product_constructor():
    product_controller = ProductController()
    product = view_register_product()
    response = product_controller.register_product(product)
    response_products(response)

