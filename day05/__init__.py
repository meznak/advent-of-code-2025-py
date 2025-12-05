'''
Advent of Code 2025 Day 05
Cafeteria
'''

SAMPLE_SOLUTIONS = [3]


def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    ranges = []
    ids = []

    first_section = True

    for item in dataset:
        if item == '':
            first_section = False
            continue

        if first_section:
            ranges.append([int(x) for x in item.split('-')])
        else:
            ids.append(int(item))

    return [ranges, ids]


def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    ranges = dataset[0]
    ids = dataset[1]

    fresh_count = 0

    for id in ids:
        for range in ranges:
            if range[0] <= id <= range[1]:
                fresh_count += 1
                break

    return fresh_count


def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    for item in dataset:
        # TODO: Build solution
        pass
