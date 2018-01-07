"""
- Implement a function, called is_increasing(seq) where seq is a list of integers. The function should return True,
if the given sequence is monotonously increasing. And before you skip this problem, because of the math terminology,
let me explain: A sequence is monotonously increasing if for every two elements a and b, that are next to each other
(a is before b), we have a < b. For example, [1,2,3,4,5] is monotonously increasing, but [1,2,3,4,5,1] is not.


- Implement a function, called is_decreasing(seq) where seq is a list of integers. The function should return True,
if the given sequence is monotonously decreasing. And before you skip this problem, because of the math terminology,
let me explain: A sequence is monotonously decreasing if for every two elements a and b, that are next to each other
(a is before b), we have a > b. For example, [5,4,3,2,1] is monotonously decreasing, but [1,2,3,4,5,1] is not.
"""


def is_increasing(seq):
    length = len(seq)
    if length == 0:
        return False

    for i in range(length - 1):
        if seq[i] >= seq[i + 1]:
            return False

    return True


def is_decreasing(seq):
    length = len(seq)
    if length == 0:
        return False

    for i in range(length - 1):
        if seq[i] <= seq[i + 1]:
            return False

    return True


def main():
    sequence_string = input(
        "Enter the numbers of a sequence separated by comma to get if it's increasing, decreasing or neither: ")
    sequence = [int(x.strip()) for x in sequence_string.split(',')]
    print('The sequence is increasing: ', is_increasing(sequence))
    print('The sequence is decreasing: ', is_decreasing(sequence))


if __name__ == '__main__':
    main()
