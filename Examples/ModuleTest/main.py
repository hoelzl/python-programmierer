import printer
import names

print('Loading main.py')
print(f"__name__ is {__name__}")


def count_words(text: str) -> dict:
    words = text.lower().split()
    result = {}
    for word in words:
        count = result.get(word, 0)
        result[word] = count + 1
    return result


if __name__ == '__main__':
    print("main.py started as main program.")

    printer.print_greeting(names.get_name())

    print(count_words("It was the best of times it was the worst of times"))

