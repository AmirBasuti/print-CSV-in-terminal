import csv


def left_just(word, width):
    return word + ' ' * (width - len(word))


def right_just(word, width):
    return ' ' * (width - len(word)) + word


def center_just(word, width):
    left = (width - len(word)) // 2
    right = width - len(word) - left
    return ' ' * left + word + ' ' * right


def calculate_widths(data):
    column_widths = [0] * len(data[0])
    for row in data:
        for i, cell in enumerate(row):
            column_widths[i] = max(column_widths[i], len(cell))
    return column_widths


def print_table(data):
    column_widths = calculate_widths(data)
    print('-' * (sum(column_widths)+4))
    for i, cell in enumerate(data.pop(0)):
        print(center_just(cell, column_widths[i]), end='|')

    print('\n'+'-' * (sum(column_widths)+4))
    for row in data:
        for i, cell in enumerate(row):
            print(center_just(cell, column_widths[i]), end='|')
        print()
    print('-' * (sum(column_widths)+4))

def read_csv(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        return [row for row in reader]


data = read_csv('text.csv')
print_table(data)
