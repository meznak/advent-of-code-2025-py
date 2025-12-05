'''
Advent of Code 2025 Day 05
Cafeteria
'''

SAMPLE_SOLUTIONS = [3, 14]


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

    ranges = dataset[0]
    ranges.sort()
    new_ranges = []
    changed = True

    while changed:
        changed = False

        for range in ranges:
            for other in ranges:
                if range == other:
                    continue
                if range[0] < other[0] and other[0] < range[1] < other[1]:
                    new_ranges.append([range[0], other[1]])
                    changed = True
                    break

            if not changed:
                new_ranges.append(range)
        ranges = new_ranges
        new_ranges = []


    fresh_count = 0

    for range in ranges:
        fresh_count += range[1] - range[0] + 1

    return fresh_count