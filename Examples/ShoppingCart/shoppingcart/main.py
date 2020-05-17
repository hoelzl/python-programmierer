import argparse

from shoppingcart.shopping_cart import ShoppingCart


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Manage a shopping cart")

    parser.add_argument('file')
    opts = parser.add_mutually_exclusive_group(required=True)
    opts.add_argument('--create', action='store_true')
    opts.add_argument('--csv-file',
                      dest='csv_file',
                      type=argparse.FileType('r'),
                      help="a CSV file containing one shopping cart entry "
                           "per line")
    opts.add_argument('--add', nargs=4,
                      metavar=('id', 'name', 'price', 'num'),
                      help="add a new item to the shopping cart")
    opts.add_argument('--delete', nargs=4,
                      metavar=('id', 'name', 'price', 'num'),
                      help="delete the first matching item")
    opts.add_argument('--list', action='store_true')

    return parser.parse_args()


def main():
    args = get_args()
    save_cart = True
    if args.create:
        with open(args.file, 'wb'):
            pass
    else:
        if csv_file := args.csv_file:
            shopping_cart = ShoppingCart.from_csv(csv_file)
        else:
            with open(args.file, 'rb') as file:
                shopping_cart = ShoppingCart.load_from_file(file)
        if args.add:
            art_num, art_name, price_per_item, number_of_items = args.add
            shopping_cart.add({
                'article_number': art_num,
                'article_name': art_name,
                'price_per_item': float(price_per_item),
                'number_of_items': int(number_of_items)
            })
        elif args.delete:
            art_num, art_name, price_per_item, number_of_items = args.delete
            shopping_cart.delete({
                'article_number': art_num,
                'article_name': art_name,
                'price_per_item': float(price_per_item),
                'number_of_items': int(number_of_items)
            })
        elif args.list:
            print(shopping_cart)

        if save_cart:
            with open(args.file, 'wb') as file:
                shopping_cart.save_to_file(file)


if __name__ == '__main__':
    main()
