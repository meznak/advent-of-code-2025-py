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
    new_ranges = []
    changed = True

    while changed:
        changed = False
        skip_next = 0
        length = len(ranges)
        ranges.sort()

        for i in range(length - 1):
            curr = ranges[i]

            if skip_next > 0:
                skip_next -= 1
                continue

            for j in range(i + 1, length):
                other = ranges[j]
                if curr[1] >= other[0]:
                    curr[1] = other[1]
                    changed = True
                    skip_next += 1
                elif j == length - 1 and j != i + skip_next:
                    new_ranges.append(other)
                else:
                    break
            new_ranges.append(curr)

        if changed:
            ranges = new_ranges
            new_ranges = []

    fresh_count = 0

    for i in ranges:
        fresh_count += i[1] - i[0] + 1

    return fresh_count