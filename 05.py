import copy
from collections import namedtuple
from itertools import chain


Point = namedtuple('Point', 'x y')
Line = namedtuple('Line', 'start end')


def get_data():
    f = open('05_input.txt', 'r')
    data_str = f.read()
    data_str_split = data_str.split('\n')

    def update_max_values(point):
        new_max_x_value, new_max_y_value = max_x_value, max_y_value
        if point.x > max_x_value:
            new_max_x_value = point.x
        if point.y > max_y_value:
            new_max_y_value = point.y
        return new_max_x_value, new_max_y_value

    lines = []
    max_x_value = 0
    max_y_value = 0
    for line in data_str_split:
        if not line:
            continue
        point_pairs = line.split(' -> ')

        start_pair = point_pairs[0].split(',')
        start_point = Point(int(start_pair[0]), int(start_pair[1]))
        max_x_value, max_y_value = update_max_values(start_point)

        end_pair = point_pairs[1].split(',')
        end_point = Point(int(end_pair[0]), int(end_pair[1]))
        max_x_value, max_y_value = update_max_values(end_point)

        lines.append(Line(start_point, end_point))

    return lines, max_x_value, max_y_value


# Part 1
def create_overlap_grid(lines, max_x_value, max_y_value):
    grid = [['.' for x in range(max_x_value + 1)] for _ in range(max_y_value + 1)]

    for line in lines:
        if line.start.x == line.end.x:
            bounds = sorted([line.start.y, line.end.y])
            for y_index in range(bounds[0], bounds[1] + 1):
                current_value = grid[y_index][line.start.x]
                grid[y_index][line.start.x] = current_value + 1 if current_value != '.' else 1
            pass
        elif line.start.y == line.end.y:
            bounds = sorted([line.start.x, line.end.x])
            for x_index in range(bounds[0], bounds[1] + 1):
                current_value = grid[line.start.y][x_index]
                grid[line.start.y][x_index] = current_value + 1 if current_value != '.' else 1

    return grid


# Part 2
def create_overlap_grid_2(lines, max_x_value, max_y_value):
    grid = [['.' for x in range(max_x_value + 1)] for _ in range(max_y_value + 1)]

    for line in lines:
        if line.start.x == line.end.x:
            bounds = sorted([line.start.y, line.end.y])
            for y_index in range(bounds[0], bounds[1] + 1):
                current_value = grid[y_index][line.start.x]
                grid[y_index][line.start.x] = current_value + 1 if current_value != '.' else 1
            pass
        elif line.start.y == line.end.y:
            bounds = sorted([line.start.x, line.end.x])
            for x_index in range(bounds[0], bounds[1] + 1):
                current_value = grid[line.start.y][x_index]
                grid[line.start.y][x_index] = current_value + 1 if current_value != '.' else 1
        else:
            slope = int((line.end.y - line.start.y) / (line.end.x - line.start.x))
            sorted_points = sorted([line.start, line.end], key=lambda point: point.x)
            x, y = sorted_points[0].x, sorted_points[0].y

            while x != sorted_points[1].x and y != sorted_points[1].y:
                current_value = grid[y][x]
                grid[y][x] = current_value + 1 if current_value != '.' else 1

                if slope == 1:
                    x += slope
                    y += slope
                elif slope == -1:
                    x -= slope
                    y += slope
            current_value = grid[y][x]
            grid[y][x] = current_value + 1 if current_value != '.' else 1

    return grid


def get_number_of_overlapping_points():
    lines, max_x_value, max_y_value = get_data()
    # grid = create_overlap_grid(lines, max_x_value, max_y_value)
    grid = create_overlap_grid_2(lines, max_x_value, max_y_value)

    flattened_grid = list(chain.from_iterable(grid))
    return len([value for value in flattened_grid if type(value) == int and value >= 2])


print(get_number_of_overlapping_points())
