import argparse

from todos.todo_list import TodoList


def get_args():
    parser = argparse.ArgumentParser('Manage a TODO list.')

    # Cannot use a file type, since the required mode will only be known later
    parser.add_argument('file')
    opts = parser.add_mutually_exclusive_group(required=True)
    opts.add_argument('--create', action='store_true')
    opts.add_argument('--add', nargs=2, metavar=('title', 'priority'))
    opts.add_argument('--delete', metavar='title')
    opts.add_argument('--mark-completed', metavar='title')
    opts.add_argument('--delete-all-completed', action='store_true')
    opts.add_argument('--list', action='store_true')

    return parser.parse_args()


def main():
    args = get_args()
    if args.create:
        with open(args.file, 'wb'):
            pass
    else:
        save_todos = True
        with open(args.file, 'rb') as file:
            todos = TodoList.load_from_file(file)
        if args.add:
            title, priority = args.add
            todos.add(title, int(priority))
        elif args.delete is not None:
            todos.delete(args.delete)
        elif args.mark_completed is not None:
            todos.mark_completed(args.mark_completed)
        elif args.delete_all_completed:
            todos.delete_all_completed()
        else:
            save_todos = False
            print(todos)
        if save_todos:
            with open(args.file, 'wb') as file:
                todos.save_to_file(file)


if __name__ == '__main__':
    main()
