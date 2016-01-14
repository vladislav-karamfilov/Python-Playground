"""
Implement the function max_consecutive(items), which takes a list of things and returns an integer - the count of
elements in the longest subsequence of equal consecutive elements.

For example, in the list [1, 2, 3, 3, 3, 3, 4, 3, 3], the result is 4, where the longest subsequence is formed
by 3, 3, 3, 3
"""


def max_consecutive(items):
    max_consecutive_items_count, current = 0, 1

    for i in range(1, len(items)):
        if items[i] == items[i - 1]:
            current += 1
        else:
            if current > max_consecutive_items_count:
                max_consecutive_items_count = current
            
            current = 1

    if current > max_consecutive_items_count:
        max_consecutive_items_count = current

    return max_consecutive_items_count


def main():
    print('***Gets the maximum count of equal consecutive elements in a list***')
    print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
    print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))
    print(max_consecutive([-1, 0, 1]))
    print(max_consecutive([1, -1, 1, 2, 2, 3, 24, 5, 5, 225, 5]))


if __name__ == '__main__':
    main()
