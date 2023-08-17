from src.views.view_options import show_options
from src.main.constructor.list_all_products_constructor import list_all_products_constructor
from src.main.constructor.list_clients_by_state import list_clients_by_state_constructor
from src.main.constructor.product_delete_constructor import product_delete_constructor
from src.main.constructor.register_client_constructor import register_client_constructor
from src.main.constructor.register_product_constructor import register_product_constructor
from src.utils.utils import clear_terminal


def start_program():
    is_running = True

    while is_running:
        option = show_options()

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
            list_clients_by_state_constructor()
            clear_terminal(3)
        elif option.strip() == "5":
            product_delete_constructor()
            clear_terminal(3)
        elif option.strip() == "6":
            is_running = False

        else:
            print("Opção Inválida, Tente Novamente!")

    print("Fim do Programa!")
