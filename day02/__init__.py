'''
Advent of Code 2025 Day 02
Gift Shop
'''

SAMPLE_SOLUTIONS = [1227775554, 4174379265]


def parse_data(dataset: list) -> list:
    '''Interpret string data'''

    output = []

    ranges = dataset[0].split(',')

    for item in ranges:
        range = item.split('-')
        output.append(range)

    return output


def solve_1(dataset: list) -> int:
    '''Solve part 1'''

    invalid_sum = 0

    for item in dataset:
        for number in range(int(item[0]), int(item[1]) + 1):
            numstr = str(number)
            length = len(numstr)
            half = length // 2
            match = True

            if length % 2 == 1:
                continue

            for pos in range(half):
                if numstr[pos] != numstr[half + pos]:
                    match = False
                    break

            if match:
                invalid_sum += number

    return invalid_sum



def solve_2(dataset: list) -> int:
    '''Solve part 2'''

    invalid_sum = 0

    for item in dataset:
        for number in range(int(item[0]), int(item[1]) + 1):
            numstr = str(number)
            length = len(numstr)
            half = length // 2

            for segment_length in range(1, half + 1):
                match = True
                first_segment = numstr[:segment_length]
                for segment_start in range(segment_length, length, segment_length):
                    segment_end = segment_start + segment_length
                    next_segment = numstr[segment_start:segment_end]
                    if first_segment != next_segment:
                        match = False
                        break

                if match:
                    invalid_sum += number
                    break

    return invalid_sum