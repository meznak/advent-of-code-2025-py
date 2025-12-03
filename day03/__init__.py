'''
Advent of Code 2025 Day 03
Lobby
'''

# TODO: Add sample solutions
SAMPLE_SOLUTIONS = [357]


def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    return dataset


def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    joltage = 0

    for item in dataset:
        # Find the largest first digit
        largest_first = '0'
        largest_first_pos = -1
        for pos in range(len(item) - 1):
            if item[pos] > largest_first:
                largest_first = item[pos]
                largest_first_pos = pos

        # Find the largest second digit
        largest_second = '0'
        largest_second_pos = -1
        for pos in range(largest_first_pos + 1, len(item)):
            if item[pos] > largest_second:
                largest_second = item[pos]
                largest_second_pos = pos

        joltage += int(largest_first + largest_second)

    return joltage

def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    for item in dataset:
        # TODO: Build solution
        pass
