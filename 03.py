import copy


def get_diagnostic_number_list():
    f = open('03_input.txt', 'r')
    measurements_str = f.read()
    measurements = measurements_str.split('\n')

    return [measurement for measurement in measurements if measurement]


# Part 1
def get_power_consumption():
    measurements = get_diagnostic_number_list()

    gamma_rate = ''
    epsilon_rate = ''

    for i in range(len(measurements[0])):
        zero_sum = 0
        one_sum = 0
        for measurement in measurements:
            match measurement[i]:
                case '1':
                    one_sum += 1
                case '0':
                    zero_sum += 1

        if zero_sum > one_sum:
            gamma_rate += '0'
            epsilon_rate += '1'
        elif zero_sum < one_sum:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            raise ValueError('Should not happen')

    gamma_rate_int = int(gamma_rate, 2)
    epsilon_rate_int = int(epsilon_rate, 2)

    return gamma_rate_int * epsilon_rate_int


# print(get_power_consumption())


# Part 2
def get_life_support_rating():
    measurements = get_diagnostic_number_list()
    measurements_2 = get_diagnostic_number_list()

    oxygen_generator_rating = ''
    co2_scrubber_rating = ''

    for i in range(len(measurements[0])):
        zero_sum = 0
        one_sum = 0
        for measurement in measurements:
            match measurement[i]:
                case '1':
                    one_sum += 1
                case '0':
                    zero_sum += 1

        if zero_sum > one_sum:
            new_list = [measurement for measurement in measurements if measurement[i] == '0']
            oxygen_generator_rating += '0'
        elif zero_sum < one_sum:
            new_list = [measurement for measurement in measurements if measurement[i] == '1']
            oxygen_generator_rating += '1'
        else:
            new_list = [measurement for measurement in measurements if measurement[i] == '1']
            oxygen_generator_rating += '1'

        del measurements[:]
        measurements = copy.deepcopy(new_list)
        if len(measurements) == 1:
            oxygen_generator_rating = measurements[0]
            break

    oxygen_generator_rating_int = int(oxygen_generator_rating, 2)

    for i in range(len(measurements_2[0])):
        zero_sum = 0
        one_sum = 0
        for measurement in measurements_2:
            match measurement[i]:
                case '1':
                    one_sum += 1
                case '0':
                    zero_sum += 1

        if zero_sum > one_sum:
            new_list = [measurement for measurement in measurements_2 if measurement[i] == '1']
            co2_scrubber_rating += '1'
        elif zero_sum < one_sum:
            new_list = [measurement for measurement in measurements_2 if measurement[i] == '0']
            co2_scrubber_rating += '0'
        else:
            new_list = [measurement for measurement in measurements_2 if measurement[i] == '0']
            co2_scrubber_rating += '0'

        del measurements_2[:]
        measurements_2 = copy.deepcopy(new_list)
        if len(measurements_2) == 1:
            co2_scrubber_rating = measurements_2[0]
            break

    co2_scrubber_rating_int = int(co2_scrubber_rating, 2)

    return oxygen_generator_rating_int * co2_scrubber_rating_int


print(get_life_support_rating())
