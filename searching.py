import json
import os
import time


# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """

    if field not in { "unordered_numbers", 'ordered_numbers', 'dna_sequence'}:
        return None

    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, 'r') as json_file:
        seq = json.load(json_file)

    return seq[field]


def linear_searching(seq, number):
    count = 0
    positions = []
    index = 0

    while index < len(seq):
        if seq[index] == number:
            count += 1
            positions.append(index)
        index += 1

    slovnik = {'positions': positions, 'count': count}
    return slovnik


def pattern_search(seq, pattern):
    positions = set()
    pattern_size = len(pattern)
    left_index = 0
    right_index = pattern_size

    while right_index < len(seq):
        for idx in range(pattern_size):
            if pattern[idx] != seq[left_index + idx]:
                break
        else:
            positions.add(left_index + pattern_size // 2)

        left_index += 1
        right_index += 1

    return positions


def binary_search(seq, number):

    left, right = (0, len(seq) - 1)

    while left <= right:
        middle = (right + left) // 2

        if number < seq[middle]:
            right = middle - 1
        elif number > seq[middle]:
            left = middle + 1
        else:
            total_time = time.time()
            return middle, total_time
    return None


def main():
    file_name = 'sequential.json'

    seq = read_data(file_name, field='ordered_numbers')
    print(seq)

    # number = linear_searching(seq, 0)
    # print(number)

    # positions = pattern_search(seq, 'ATA')
    # print(positions)

    index = binary_search(seq, -3)
    print(index)


if __name__ == '__main__':
    main()