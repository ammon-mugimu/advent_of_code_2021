
def get_change_list():
    f = open('02_input.txt', 'r')
    measurements_str = f.read()
    measurements = measurements_str.split('\n')

    result = []
    for measurement in measurements:
        if not measurement:
            continue
        split_measurement = measurement.split(' ')
        result.append((split_measurement[0], int(split_measurement[1])))
    return result


# Part 1
def get_position_multiple():
    measurements = get_change_list()

    horizontal_distance = 0
    depth = 0

    for measurement in measurements:
        match measurement[0]:
            case 'forward':
                horizontal_distance += measurement[1]
            case 'down':
                depth += measurement[1]
            case 'up':
                depth -= measurement[1]

    return horizontal_distance * depth


print(get_position_multiple())


# Part 2
def get_position_multiple_2():
    measurements = get_change_list()

    horizontal_distance = 0
    depth = 0
    aim = 0

    for measurement in measurements:
        direction = measurement[0]
        value = measurement[1]

        match direction:
            case 'forward':
                horizontal_distance += value
                depth += aim * value
            case 'down':
                aim += value
            case 'up':
                aim -= value

    return horizontal_distance * depth


print(get_position_multiple_2())
