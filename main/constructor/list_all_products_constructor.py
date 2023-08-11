from src.controllers.products.products_controller import ProductController
from src.views.view_all_products import list_all_products


def list_all_products_constructor():
    products_controller = ProductController()
    products = products_controller.list_products()
    list_all_products(products)
