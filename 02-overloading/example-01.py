class EshopCart:
    def __init__(self, buyer):
        self.buyer = buyer
        self.products = []
        self.total = 0.0

    def add_product(self, name, price):
        self.products.append(name)
        self.total += price

    def __len__(self):
        return len(self.products)


if __name__ == "__main__":
    cart = EshopCart("Ann")
    cart.add_product("jeans", 30.0)
    print(f"Cart's length: {len(cart)}")
