from src.controllers.products.products_controller import ProductController
from src.views.view_deleted_product import view_product_deleted, view_product_to_delete


def product_delete_constructor():
    product_controller = ProductController()

    product_to_delete = view_product_to_delete()
    response = product_controller.remove_product(product_to_delete)
    view_product_deleted(response)
