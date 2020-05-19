import printer
import names

print('Loading foo.py')
print(f"__name__ is {__name__}")

if __name__ == '__main__':
    print("foo.py started as main program.")
    printer.print_greeting(names.get_name())
