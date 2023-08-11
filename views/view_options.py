def show_options():
    view = """

Bem-Vindo ao Sistema, o que deseja?

(1) - Cadastrar cliente por nome, telefone e estado
(2) - Cadastrar produto da loja por nome e sabor (ex: Bolo de Chocolate / Bolo de Morango)
(3) - Apresentar todos os produtos cadastrados
(4) - Apresentar todos os clientes de um determinado estado
(5) - Deletar um produto cadastrado

"""
    option = input(view)
    return option
