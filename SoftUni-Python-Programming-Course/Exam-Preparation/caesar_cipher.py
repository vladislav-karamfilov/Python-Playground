# Problem description: http://python3.softuni.bg/student/lecture/assignment/56bc86d37e4f59b64bb7e6b6/

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def _normalize_key(key):
    alphabet_length = len(ALPHABET)

    if key > alphabet_length:
        return key % alphabet_length

    return key


def _get_corresponding_cipher_alphabet(alphabet, key):
    result = {}

    alphabet_length = len(alphabet)
    for i, letter in enumerate(alphabet):
        if key + i < alphabet_length:
            result[letter] = alphabet[key + i]
        else:
            result[letter] = alphabet[key + i - alphabet_length]

    return result


def _decipher_message(message, normal_alphabet, key):
    deciphered_message_chars = []

    corresponding_cipher_alphabet = _get_corresponding_cipher_alphabet(
        normal_alphabet, key)
    for char in message:
        if char in corresponding_cipher_alphabet:
            deciphered_message_chars.append(
                corresponding_cipher_alphabet[char])
        else:
            deciphered_message_chars.append(char)

    return ''.join(deciphered_message_chars)


def main():
    try:
        key = _normalize_key(int(input()))
        message = input()

        print(_decipher_message(message, ALPHABET, key))
    except:
        print('INVALID INPUT')


if __name__ == '__main__':
    main()
