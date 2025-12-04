'''
Advent of Code 2025 Day 04
Printing Department
'''

from shared.helpers import get_eight_neighbors


SAMPLE_SOLUTIONS = [13, 43]


def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    return dataset


def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    rows = len(dataset)
    cols = len(dataset[0])
    accessible_rolls = 0

    for row in range(rows):
        for col in range(cols):
            neighbor_rolls = 0

            if dataset[row][col] == '@':
                neighbors = get_eight_neighbors(dataset, (row, col))
                for neighbor in neighbors:
                    if dataset[neighbor[0]][neighbor[1]] == '@':
                        neighbor_rolls += 1

                if neighbor_rolls < 4:
                    accessible_rolls += 1

    return accessible_rolls


def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    rows = len(dataset)
    cols = len(dataset[0])
    new_dataset = []
    prev_accessible_rolls = -1
    accessible_rolls = 0

    while accessible_rolls != prev_accessible_rolls:
        prev_accessible_rolls = accessible_rolls

        for row in range(rows):
            new_dataset.append('')
            for col in range(cols):
                neighbor_rolls = 0

                if dataset[row][col] == '@':
                    neighbors = get_eight_neighbors(dataset, (row, col))
                    for neighbor in neighbors:
                        if dataset[neighbor[0]][neighbor[1]] == '@':
                            neighbor_rolls += 1

                    if neighbor_rolls < 4:
                        accessible_rolls += 1
                        new_dataset[row] += '.'
                    else:
                        new_dataset[row] += '@'
                else:
                    new_dataset[row] += '.'

        dataset = new_dataset
        new_dataset = []


    return accessible_rolls