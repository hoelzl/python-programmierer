import csv
from io import StringIO

from shopping_cart_entry import ShoppingCartEntry


class ShoppingCart:
    def __init__(self, entries):
        self.entries = entries

    @staticmethod
    def from_csv(file):
        """
        Constructor for Shopping carts

        Takes a CSV file where each line contains the following fields:
        - article number
        - article name
        - price per item
        - number of items
        in this order.
        Returns a shopping cart containing these entries
        """
        reader = csv.reader(file)
        entries = []
        for art_nr, name, ppi, num in reader:
            entries.append(ShoppingCartEntry(article_number=art_nr,
                                             article_name=name,
                                             price_per_item=float(ppi),
                                             number_of_items=int(num)))
        return ShoppingCart(entries)

    @property
    def total_price(self):
        """Compute the total price of all items in the cart"""
        result = 0.0
        for entry in self.entries:
            result += entry.total_price
        return result

    def __str__(self):
        stream = StringIO()
        print(f"Shopping cart with {len(self.entries)} "
              f"{'entry' if len(self.entries) == 1 else 'entries'}:",
              file=stream)
        for item in self.entries:
            print(f"  {item!s}", file=stream)
        print(f"Total: {self.total_price}", file=stream)
        return stream.getvalue()

    def __repr__(self):
        return f"ShoppingCart({self.entries!r})"
