import copy
from collections import Counter

def get_data():
    f = open('06_input.txt', 'r')
    data_str = f.read()
    data_str_split = data_str.split('\n')
    numbers_str = data_str_split[0].split(',')

    return [int(number_str) for number_str in numbers_str]


def num_spawned_fish(days):
    fish_days_spawn = get_data()

    def get_new_value(current):
        if current == 0:
            return 6
        return current - 1

    new_fish = []
    for day in range(days):
        fish_days_spawn.extend(new_fish)
        new_fish = copy.deepcopy([])

        for index, fish_days in enumerate(fish_days_spawn):
            new_value = get_new_value(fish_days)
            if new_value == 0:
                new_fish.append(9)
            fish_days_spawn[index] = new_value

    return fish_days_spawn


# Part 2 optimization
def num_spawned_fish_2(days):
    fish_days_spawn = get_data()
    counter = Counter(fish_days_spawn)

    counter[0] = 0
    counter[8] = 0

    for day in range(days):
        num_zero_days_left = counter[0]
        counter[0] = 0

        for num_days_left in range(1, 9):
            fish_count = counter[num_days_left]
            counter[num_days_left - 1] = fish_count

        counter[6] += num_zero_days_left
        counter[8] = num_zero_days_left

    return counter


result = num_spawned_fish_2(80)
print(result)
print(result.total())


result = num_spawned_fish_2(256)
print(result)
print(result.total())
