'''
Advent of Code 2025 Day 06
Trash Compactor
'''
import numpy as np

SAMPLE_SOLUTIONS = [4277556]


def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    numbers = []
    operations = dataset.pop().split()


    for item in dataset:
        line = []
        for number in item.split():
            line.append(int(number))
        numbers.append(line)

    transposed = np.array(numbers).T.tolist()


    return [operations, transposed]


def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    operations = dataset[0]
    numbers = dataset[1]
    output = 0

    for col in range(len(operations)):
        result = numbers[col][0]

        if operations[col] == '+':
            for num in numbers[col][1:]:
                result += num
        else:
            for num in numbers[col][1:]:
                result *= num
        output += result

    return output


def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    for item in dataset:
        # TODO: Build solution
        pass
