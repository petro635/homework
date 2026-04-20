from models import Product

def get_all_products():
    return Product.select() # НЕ додавайте .dicts() сюди!

def get_product_by_category(category: str):
    return Product.select().where(Product.category == category)

def get_all_categories():
    return Product.select(Product.category).distinct()

def product_exist(name: str) -> bool:
    return Product.select().where(Product.name == name).exists()

def add_product(name: str, price: float, category: str):
    Product.create(name=name, price=price, category=category)

def delete_product_by_name(name: str):
    query = Product.delete().where(Product.name == name)
    query.execute()


