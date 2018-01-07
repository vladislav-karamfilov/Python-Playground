def text_after_another(first, second):
    result = first

    index = first.find(second)
    if index >= 0:
        result = first[index + len(second):]

    return result


def main():
    first = input('Enter the first text: ')
    second = input('Enter the second text: ')

    print(text_after_another(first, second))


if __name__ == '__main__':
    main()
