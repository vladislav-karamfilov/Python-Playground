"""
Lets have a set of sets:
A = { {1, 2, 3} , {4, 5, 6}, {7, 8, 9} }

A transversal T for A is a set that contains at least one element from each set of A.

For example: T = {1, 4, 7}

Implement a function is_transversal(transversal, family), which check if given set is a valid transversal
for another family of sets (set of sets).
"""


def is_transversal(transversal, family):
    for set in family:
        set_contains_at_least_one_element = False
        for element in transversal:
            if element in set:
                set_contains_at_least_one_element = True
                break

        if not set_contains_at_least_one_element:
            return False

    return True


def main():
    print('***Check for transversal***')
    print(is_transversal([4, 5, 6], [[5, 7, 9], [1, 4, 3], [2, 6]]))
    print(is_transversal([1, 2], [[1, 5], [2, 3], [4, 7]]))
    print(is_transversal([2, 3, 4], [[1, 7], [2, 3, 5], [4, 8]]))


if __name__ == '__main__':
    main()
