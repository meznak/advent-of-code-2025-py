'''
Advent of Code 2025 Day 01
Secret Entrance
'''

SAMPLE_SOLUTIONS = [3, 6]


def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    output = []

    for item in dataset:
        if item != '':
            output.append((item[0], int(item[1:])))

    return output


def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    number = 50
    zeroes = 0

    for item in dataset:
        if item[0] == 'R':
            number += item[1]
        else:
            number -= item[1]

        number %= 100

        if number == 0:
            zeroes += 1

    return zeroes


def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    number = 50
    zeroes = 0

    for item in dataset:
        if item[0] == 'R':
            number += item[1]
            zeroes += number // 100
            number %= 100
        else:
            if number == 0:
                zeroes -= 1
            number -= item[1]
            zeroes += (number // -100) + 1
            number %= 100

    return zeroes