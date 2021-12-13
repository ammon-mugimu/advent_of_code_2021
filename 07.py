import sys
from collections import Counter
from itertools import accumulate


def get_data():
    f = open('07_input.txt', 'r')
    data_str = f.read()
    numbers_str = data_str.split(',')

    return [int(number_str) for number_str in numbers_str]


def get_optimal_fuel_to_use():
    horizontal_positions = get_data()
    smallest_value = min(horizontal_positions)
    largest_value = max(horizontal_positions)
    optimal_fuel_amount = sys.maxsize
    counter = Counter(horizontal_positions)

    for value in range(smallest_value, largest_value + 1):
        temp_fuel_amount = 0
        for horizontal_position, num_submarines in counter.items():
            temp_fuel_amount += abs(value - horizontal_position) * num_submarines

        if temp_fuel_amount < optimal_fuel_amount:
            optimal_fuel_amount = temp_fuel_amount

    return optimal_fuel_amount


def get_optimal_fuel_to_use_2():
    horizontal_positions = get_data()
    smallest_value = min(horizontal_positions)
    largest_value = max(horizontal_positions)

    step_costs = [i for i in range(largest_value + 1)]
    cumulative_steps = list(accumulate(step_costs))
    optimal_fuel_amount = sys.maxsize
    counter = Counter(horizontal_positions)

    for value in range(smallest_value, largest_value + 1):
        temp_fuel_amount = 0
        for horizontal_position, num_submarines in counter.items():
            number_of_steps = abs(value - horizontal_position)
            cost_of_steps = cumulative_steps[number_of_steps]
            temp_fuel_amount += cost_of_steps * num_submarines

        if temp_fuel_amount < optimal_fuel_amount:
            optimal_fuel_amount = temp_fuel_amount

    return optimal_fuel_amount


result = get_optimal_fuel_to_use_2()
print(result)
