from collections import defaultdict


def get_data():
    f = open('11_input.txt', 'r')
    data_str = f.read()
    connections = data_str.split('\n')

    adjacency_list = defaultdict(list)
    for connection in connections:
        pair = connection.split('-')
        first, second = pair[0], pair[1]
        if second != 'start' and first != 'end':
            adjacency_list[first].append(second)
        if first != 'start' and second != 'end':
            adjacency_list[second].append(first)

    return adjacency_list


def get_paths(adjacency_list, curr_node, visited_small_caves, curr_solution, solutions):
    if curr_node == 'end':
        curr_solution_str = ','.join(curr_solution)
        solutions.add(curr_solution_str)
        return

    neighbors = adjacency_list[curr_node]
    for neighbor in neighbors:
        if neighbor not in visited_small_caves:
            curr_solution.append(neighbor)
            if neighbor.islower():
                visited_small_caves.add(neighbor)

            get_paths(adjacency_list, neighbor, visited_small_caves, curr_solution, solutions)

            curr_solution.pop()
            if neighbor.islower():
                visited_small_caves.remove(neighbor)


def get_all_paths():
    mapping = get_data()

    visited_small_caves = {'start'}
    curr_solution = ['start']
    solutions = set()
    get_paths(mapping, 'start', visited_small_caves, curr_solution, solutions)

    return solutions, len(solutions)


# result = get_all_paths()
# print(result[0])
# print(result[1])


def get_paths_2(adjacency_list, curr_node, visited_small_caves, curr_solution, solutions, small_cave_exception):
    if curr_node == 'end':
        curr_solution_str = ','.join(curr_solution)
        solutions.add(curr_solution_str)
        return

    neighbors = adjacency_list[curr_node]
    for neighbor in neighbors:
        visits = small_cave_exception.get(neighbor, -1)
        if neighbor not in visited_small_caves or visits == 1:
            curr_solution.append(neighbor)
            if neighbor.islower():
                visited_small_caves.add(neighbor)
                if neighbor in small_cave_exception:
                    small_cave_exception[neighbor] += 1

            get_paths_2(adjacency_list, neighbor, visited_small_caves, curr_solution, solutions, small_cave_exception)

            curr_solution.pop()
            if neighbor.islower():
                if neighbor in visited_small_caves:
                    visited_small_caves.remove(neighbor)
                if neighbor in small_cave_exception:
                    small_cave_exception[neighbor] -= 1


def get_all_paths_2():
    mapping = get_data()

    visited_small_caves = {'start'}
    curr_solution = ['start']
    solutions = set()
    small_caves = [cave for cave in mapping.keys() if cave.islower() and cave != 'start' and cave != 'end']

    for small_cave in small_caves:
        get_paths_2(mapping, 'start', visited_small_caves, curr_solution, solutions, {small_cave: 0})

    return solutions, len(solutions)


result = get_all_paths_2()
# print(result[0])
print(result[1])
