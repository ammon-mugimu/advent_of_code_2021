import heapq
from functools import reduce


def get_data():
    f = open('09_input.txt', 'r')
    data_str = f.read()
    numbers_str = data_str.split('\n')

    arr = []
    for row in numbers_str:
        arr.append([int(number_str) for number_str in row])

    return arr


def get_risk_level_sum():
    arr = get_data()

    low_points = []
    for index_y, row in enumerate(arr):
        for index_x, val in enumerate(row):
            neighbors = [
                (index_y, index_x + 1),
                (index_y, index_x - 1),
                (index_y - 1, index_x),
                (index_y + 1, index_x)
            ]
            valid_neighbors = [
                pair
                for pair in neighbors
                if 0 <= pair[0] < len(arr) and 0 <= pair[1] < len(row)
            ]
            larger_or_equal_neighbors = [
                arr[neighbor[0]][neighbor[1]]
                for neighbor in valid_neighbors
                if val < arr[neighbor[0]][neighbor[1]]
            ]
            if len(valid_neighbors) == len(larger_or_equal_neighbors):
                low_points.append(val)

    risk_levels = [val + 1 for val in low_points]
    return sum(risk_levels)


# result = get_risk_level_sum()
# print(result)


def get_three_largest_basin_multiple():
    arr = get_data()

    low_points = []
    for index_y, row in enumerate(arr):
        for index_x, val in enumerate(row):
            neighbors = [
                (index_y, index_x + 1),
                (index_y, index_x - 1),
                (index_y - 1, index_x),
                (index_y + 1, index_x)
            ]
            valid_neighbors = [
                pair
                for pair in neighbors
                if 0 <= pair[0] < len(arr) and 0 <= pair[1] < len(row)
            ]
            larger_or_equal_neighbors = [
                arr[neighbor[0]][neighbor[1]]
                for neighbor in valid_neighbors
                if val < arr[neighbor[0]][neighbor[1]]
            ]
            if len(valid_neighbors) == len(larger_or_equal_neighbors):
                low_points.append((index_y, index_x))

    heap = []
    for point in low_points:
        # BFS
        visited = {point}
        queue = [point]

        while queue:
            point_from_queue = queue.pop(0)
            index_y = point_from_queue[0]
            index_x = point_from_queue[1]
            neighbors = [
                (index_y, index_x + 1),
                (index_y, index_x - 1),
                (index_y - 1, index_x),
                (index_y + 1, index_x)
            ]
            valid_neighbors = [
                pair
                for pair in neighbors
                if 0 <= pair[0] < len(arr)
                and 0 <= pair[1] < len(row)
                and arr[pair[0]][pair[1]] < 9
            ]
            for neighbor in valid_neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        if len(heap) == 3:
            heapq.heappushpop(heap, len(visited))
        else:
            heapq.heappush(heap, len(visited))

    return reduce((lambda x, y: x * y), heap)


result = get_three_largest_basin_multiple()
print(result)
