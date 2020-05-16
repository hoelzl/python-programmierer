import argparse

from shopping_cart import ShoppingCart


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a shopping cart")
    parser.add_argument('--csv-file',
                        dest='csv_file',
                        type=argparse.FileType('r'),
                        help="a CSV file containing one shopping cart entry "
                             "per line")
    return parser.parse_args()


def main():
    args = get_args()
    if csv_file := args.csv_file:
        shopping_cart = ShoppingCart.from_csv(csv_file)
        print(shopping_cart)
    else:
        print("No entries provided.")


if __name__ == '__main__':
    main()
