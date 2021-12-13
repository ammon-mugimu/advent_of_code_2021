from collections import defaultdict
import pprint


def get_data():
    f = open('12_input.txt', 'r')
    data_str = f.read()
    lines = data_str.split('\n')

    max_x = -1
    max_y = -1
    pairs = []
    folding_lines = []
    for line in lines:
        if not line:
            continue
        if line[0] != 'f':
            values = line.split(',')
            pair = (int(values[0]), int(values[1]))

            if pair[0] > max_x:
                max_x = pair[0]
            if pair[1] > max_y:
                max_y = pair[1]
            pairs.append(pair)
        else:
            words = line.split(' ')
            fold_line_str = words[-1].split('=')
            folding_lines.append((fold_line_str[0], int(fold_line_str[1])))

    # populate array
    arr = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for pair in pairs:
        arr[pair[1]][pair[0]] = '#'

    return arr, folding_lines


def fold_vertically(arr, line_index):
    for y, row in enumerate(arr):
        for x, val in enumerate(row):
            diff = y - line_index
            if diff > 0 and arr[y][x] == '#':
                arr[y][x] = '.'
                arr[line_index - diff][x] = '#'


def fold_horizontally(arr, line_index):
    for y, row in enumerate(arr):
        for x, val in enumerate(row):
            diff = x - line_index
            if diff > 0 and arr[y][x] == '#':
                arr[y][x] = '.'
                arr[y][line_index - diff] = '#'


def fold_paper():
    arr, folding_lines = get_data()

    line_tuple = folding_lines[0]
    if line_tuple[0] == 'y':
        fold_vertically(arr, line_tuple[1])

    else:
        fold_horizontally(arr, line_tuple[1])

    visible_dots = 0
    for y, row in enumerate(arr):
        for x, val in enumerate(row):
            if val == '#':
                visible_dots += 1
    return visible_dots


result = fold_paper()
print(result)


def fold_paper_2():
    arr, folding_lines = get_data()

    for line_tuple in folding_lines:
        if line_tuple[0] == 'y':
            fold_vertically(arr, line_tuple[1])

            for _ in range(line_tuple[1], len(arr)):
                del arr[-1]
        else:
            fold_horizontally(arr, line_tuple[1])
            for _ in range(line_tuple[1], len(arr)):
                for index in range(len(arr)):
                    arr[index].pop()

    pp = pprint.PrettyPrinter(width=100)
    # Return array (not ideal)
    result = [row[35:40] for row in arr]
    pp.pprint(result)
    return result


result = fold_paper_2()
print(result)
