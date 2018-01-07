"""
We are going to implement a very helpful function, called group.

group takes a list of things and returns a list of group, where each group is formed by all equal
consecutive elements in the list.

For example:
group([1, 1, 1, 2, 3, 1, 1]) == [[1, 1, 1], [2], [3], [1, 1]]
group([1, 2, 1, 2, 3, 3]) == [[1], [2], [1], [2], [3, 3]]
"""


def group(items_list):
    result = []
    
    count = len(items_list)
    if count == 0:
        return result

    result.append([items_list[0]])
    
    for i in range(1, count):
        if items_list[i - 1] == items_list[i]:
            result[len(result) - 1].append(items_list[i])
        else:
            result.append([items_list[i]])

    return result


def main():
    print('***Gets a list of groups of equal consecutive elements in a list***')
    print(group([1, 2, 1, 2, 3, 3]))
    print(group([1, 1, 1, 2, 3, 1, 1]))


if __name__ == '__main__':
    main()
