import printer
import names

print('Loading foo.py')
print(f"__name__ is {__name__}")


def main():
    print("foo.py started as main program.")
    printer.print_greeting(names.get_name())


if __name__ == '__main__':
    main()
