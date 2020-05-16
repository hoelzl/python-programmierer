class ShoppingCartEntry:
    def __init__(self, article_number, article_name, price_per_item,
                 number_of_items):
        self.article_number = article_number
        self.article_name = article_name
        self.price_per_item = price_per_item
        self.number_of_items = number_of_items

    @property
    def total_price(self):
        """Compute the total price of this shopping cart entry"""
        return self.price_per_item * self.number_of_items

    def __str__(self):
        return (f"{self.number_of_items} x "
                f"{self.article_name} à {self.price_per_item}, "
                f"total {self.total_price}")

    def __repr__(self):
        return (f"ShoppingCartEntry({self.article_number!r}, "
                f"{self.article_name!r}, {self.price_per_item!r}, "
                f"{self.number_of_items!r})")
