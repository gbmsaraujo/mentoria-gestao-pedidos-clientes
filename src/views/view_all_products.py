def show_all_products(products):
    for product in products:
        print(f"* Produto: {product['name']}, Sabor: {product['flavor']}")