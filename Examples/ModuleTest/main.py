import printer
import names

print('Loading main.py')
print(f"__name__ is {__name__}")

if __name__ == '__main__':
    print("main.py started as main program.")
    printer.print_greeting(names.get_name())
