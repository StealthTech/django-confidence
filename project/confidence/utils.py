def print_formatted(s, level=0):
    print('-' * level + f'—> {s}')


def input_formatted(s, level=0):
    return input('-' * level + f'<— {s}')
