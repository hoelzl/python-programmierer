import argparse

from shoppingcart.shopping_cart import ShoppingCart


def get_args() -> (
        argparse.Namespace, argparse.ArgumentParser):
    parser = argparse.ArgumentParser(description="Manage a shopping cart")

    subparsers = parser.add_subparsers(title='subcommands',
                                       help='help for sub-commands')

    create_parser = subparsers.add_parser('create',
                                          help='Create a new shopping cart')
    create_parser.add_argument('file',
                               type=argparse.FileType('wb'),
                               help='the file to create')
    create_parser.set_defaults(command='create')

    csv_parser = subparsers.add_parser('csv', help='Load a CSV file')
    csv_parser.add_argument('file',
                            type=argparse.FileType('wb'),
                            help='the file to create')
    csv_parser.add_argument('csv_file',
                            type=argparse.FileType('r'),
                            help="a CSV file containing one shopping cart "
                                 "entry per line")
    csv_parser.set_defaults(command='csv')

    add_parser = subparsers.add_parser('add', help='add a new item')
    add_parser.add_argument('file',
                            type=argparse.FileType('r+b'),
                            help='the file to add the item to')
    add_parser.add_argument('id', help='the item ID')
    add_parser.add_argument('name', help='the item Name')
    add_parser.add_argument('price', help='the price per item', type=float)
    add_parser.add_argument('--num',
                            dest='number_of_items',
                            type=int,
                            default=1,
                            help='the number of items to add')
    add_parser.set_defaults(command='add')

    delete_parser = subparsers.add_parser('delete', help='delete an item')
    delete_parser.add_argument('file',
                               type=argparse.FileType('r+b'),
                               help='the file to delete the item from')
    delete_parser.add_argument('id', help='the item ID')
    delete_parser.add_argument('name', help='the item Name')
    delete_parser.add_argument('price', help='the price per item',
                               type=float)
    delete_parser.add_argument('--num',
                               dest='number_of_items',
                               type=int,
                               default=1,
                               help='the number of items')
    delete_parser.set_defaults(command='delete')

    list_parser = subparsers.add_parser('list', help='list the shopping cart')
    list_parser.add_argument('file',
                             type=argparse.FileType('rb'),
                             help='the file to list')
    list_parser.set_defaults(command='list')

    return parser.parse_args(), parser


def main():
    args, parser = get_args()
    save_cart = True
    try:
        if args.command == 'create':
            pass
        else:
            if args.command == 'csv':
                shopping_cart = ShoppingCart.from_csv(args.csv_file)
            else:
                shopping_cart = ShoppingCart.load_from_file(args.file)

            if args.command == 'add':
                shopping_cart.add({
                    'article_number': args.id,
                    'article_name': args.name,
                    'price_per_item': args.price,
                    'number_of_items': args.number_of_items
                })
            elif args.command == 'delete':
                shopping_cart.delete({
                    'article_number': args.id,
                    'article_name': args.name,
                    'price_per_item': args.price,
                    'number_of_items': args.number_of_items
                })
            elif args.command == 'list':
                print(shopping_cart)
                save_cart = False

            if save_cart:
                args.file.seek(0)
                shopping_cart.save_to_file(args.file)
    except AttributeError:
        parser.print_help()


if __name__ == '__main__':
    main()
