MAX_LENGTH = 10


def max_length_with_ellipsis(text):
    return ''.join([text[:MAX_LENGTH], '...']) if len(text) > MAX_LENGTH else text


def main():
    text = input('Enter some text: ')
    print(max_length_with_ellipsis(text))
    

if __name__ == '__main__':
    main()
