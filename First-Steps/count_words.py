"""
Given a list of strings, implement a function, called count_words(arr) which returns a dictionary
of the following kind: { "word" : count }

Where count is the count of occurrences of the word in the list arr.
"""


def count_words(arr):
    result = {}
    for word in arr:
        if word in result.keys():
            result[word] += 1
        else:
            result[word] = 1

    return result


def main():
    print('***Count how many times a word is present in an array***')
    print(count_words(['apple', 'banana', 'apple', 'pie']))
    print(count_words(['python', 'python', 'python', 'ruby']))


if __name__ == '__main__':
    main()
