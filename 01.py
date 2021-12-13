
def get_change_list():
    f = open('01_input.txt', 'r')
    measurements_str = f.read()
    measurements = measurements_str.split('\n')

    return [int(measurement) for measurement in measurements if measurement]


# Part 1
def get_measurement_increase_sum():
    measurements = get_change_list()

    increase_sum = 0
    for index in range(1, len(measurements)):
        if measurements[index] > measurements[index - 1]:
            increase_sum += 1
    return increase_sum


# Part 2
def get_measurement_increase_sum_2():
    measurements = get_change_list()

    increase_sum = 0
    for index in range(3, len(measurements)):
        curr_sum = sum(measurements[index - 2: index + 1])
        prev_sum = sum(measurements[index - 3: index])
        if curr_sum > prev_sum:
            increase_sum += 1
    return increase_sum


print(get_measurement_increase_sum_2())
