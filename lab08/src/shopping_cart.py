class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity=1):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if product.id in self.products:
            self.products[product.id]["quantity"] += quantity
        else:
            self.products[product.id] = {
                "product": product,
                "quantity": quantity
            }

    def remove_product(self, product_id, quantity=1):
        if product_id not in self.products:
            raise ValueError("Product not in cart")

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if self.products[product_id]["quantity"] <= quantity:
            del self.products[product_id]
        else:
            self.products[product_id]["quantity"] -= quantity

    def get_total_price(self):
        total = sum(item["product"].price * item["quantity"]
                    for item in self.products.values())
        return round(total, 2)

    def get_product_count(self):
        return sum(item["quantity"] for item in self.products.values())