from collections import namedtuple

Pair = namedtuple('Pair', 'signal_patterns four_digit_output_list')

num_segments_mapping = {
        0: 6,
        1: 2,
        2: 5,
        3: 5,
        4: 4,
        5: 5,
        6: 6,
        7: 3,
        8: 7,
        9: 6,
}


def get_data():
    f = open('08_input.txt', 'r')
    data_str = f.read()
    entry_strings = data_str.split('\n')

    pairs = []
    for entry_str in entry_strings:
        split_entry_str = entry_str.split(' | ')
        signal_patterns = split_entry_str[0].split(' ')
        four_digit_output_list = split_entry_str[1].split(' ')
        pairs.append(Pair(signal_patterns, four_digit_output_list))

    return pairs


def find_number_of_times_digits_appear():
    pairs = get_data()

    count = 0
    valid_str_lengths = {num_segments_mapping[key] for key in [1, 4, 7, 8]}
    for pair in pairs:
        for output in pair.four_digit_output_list:
            if len(output) in valid_str_lengths:
                count += 1

    return count


result = find_number_of_times_digits_appear()
print(result)


num_segment_letter_mapping = {
    0: {'a', 'b', 'c', 'e', 'f', 'g'},
    1: {'c', 'f'},
    2: {'a', 'c', 'd', 'e', 'g'},
    3: {'a', 'c', 'd', 'f', 'g'},
    4: {'b', 'c', 'd', 'f'},
    5: {'a', 'b', 'd', 'f', 'g'},
    6: {'a', 'b', 'd', 'e', 'f', 'g'},
    7: {'a', 'c', 'f'},
    8: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
    9: {'a', 'b', 'c', 'd', 'f', 'g'},
}


def get_total_of_all_output_values():
    pairs = get_data()

    output_values = []
    for pair in pairs:
        for signal_pattern in pair.signal_patterns:
            match len(signal_pattern):
                case 2:
                    one_value = {c for c in signal_pattern}
                case 3:
                    seven_value = {c for c in signal_pattern}
                case 4:
                    four_value = {c for c in signal_pattern}

        num_str = ''
        for output in pair.four_digit_output_list:
            output_set = set(output)
            match len(output_set):
                case 7:
                    num_str += '8'
                case 6:
                    union_set = output_set.union(four_value)
                    if len(union_set) == 6:
                        num_str += '9'
                        continue
                    union_set = output_set.union(one_value)
                    if len(union_set) == 7:
                        num_str += '6'
                    else:
                        num_str += '0'
                case 5:
                    union_set = output_set.union(seven_value)
                    if len(union_set) == 5:
                        num_str += '3'
                        continue
                    remainder = four_value.difference(output_set)
                    if len(remainder) == 2:
                        num_str += '2'
                    elif len(remainder) == 1:
                        num_str += '5'
                case 4:
                    num_str += '4'
                case 3:
                    num_str += '7'
                case 2:
                    num_str += '1'
        output_values.append(int(num_str))

    return sum(output_values)


result = get_total_of_all_output_values()
print(result)
