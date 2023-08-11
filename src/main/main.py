from src.views.view_options import show_options
from src.main.constructor import (
    list_all_products_constructor,
    list_clients_by_state,
    product_delete_constructor,
    register_client_constructor,
    register_product_constructor,
)
from src.utils.utils import clear_terminal


def start_program():
    is_running = True
    option = show_options()

    while is_running:
        if option.strip() == "1":
            register_client_constructor()
            clear_terminal()
        elif option.strip() == "2":
            register_product_constructor()
            clear_terminal()
        elif option.strip() == "3":
            list_all_products_constructor()
            clear_terminal(5)
        elif option.strip() == "4":
            list_clients_by_state()
        elif option.strip() == "5":
            product_delete_constructor()
            clear_terminal(3)
        elif option.strip() == "6":
            is_running = False

        else:
            print("Opção Inválida, Tente Novamente!")

    print("Fim do Programa!")
