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

    # def __iadd__(self, other):
    #     pass
    def __add__(self, other):
        self.products.extend(other.products)
        self.total += other.total
        return self

    def __lt__(self, other):
        return self.total < other.total

    def __gt__(self, other):
        return self.total > other.total

    def __eq__(self, other):
        return self.total == other.total

    def __str__(self):
        return f"EshopCart{{buyer: {self.buyer}, total: {self.total}, products: {len(self.products)}}}"


if __name__ == "__main__":
    cart = EshopCart("Ann")
    cart.add_product("bag of rice", 400)
    cart.add_product("bag of bean", 900)
    print(len(cart))

    #Create similar cart instance with new product
    cart1 = EshopCart("Ann")
    cart1.add_product("gallon of oil", 500)

    cart = cart + cart1
    print(cart.__len__())
    print(cart.__dict__)

    cart2 = EshopCart("ben")
    cart2.add_product("banana", 40)
    cart2.add_product("carrot", 90)
    print(cart2.__dict__)

    print(f"cart less than cart2 {cart2 < cart}")
    print(f"cart2  greater than cart {cart > cart2}")
    print(f"cart equals to cart2 {cart2 == cart}")
    print(str(cart))
    print(str(cart2))

