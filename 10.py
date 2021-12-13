import heapq
from functools import reduce


def get_data():
    f = open('10_input.txt', 'r')
    data_str = f.read()
    lines = data_str.split('\n')

    return [[char for char in line] for line in lines]


score_map = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
expected_matches = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

count_map = {
    ')': 0,
    ']': 0,
    '}': 0,
    '>': 0
}


def get_total_syntax_error_score():
    arr = get_data()

    for line in arr:
        stack = []
        for char in line:
            if char not in score_map.keys():
                stack.append(char)
            else:
                value = stack.pop()
                if value != expected_matches[char]:
                    count_map[char] += 1
                    break

    total_syntax_error_score = 0
    for char in score_map.keys():
        total_syntax_error_score += score_map[char] * count_map[char]
    return total_syntax_error_score


# result = get_total_syntax_error_score()
# print(result)


autocomplete_score_map = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
expected_matches_reverse = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def get_middle_autocomplete_score():
    arr = get_data()

    incomplete_lines = []
    total_scores = []
    for line in arr:
        stack = []
        invalid_line = False
        for char in line:
            if char not in score_map.keys():
                stack.append(char)
            else:
                value = stack.pop()
                if value != expected_matches[char]:
                    count_map[char] += 1
                    invalid_line = True
                    break
        if not invalid_line:
            total_score = 0
            while stack:
                value = stack.pop()
                required_character = expected_matches_reverse[value]
                total_score *= 5
                total_score += autocomplete_score_map[required_character]

            total_scores.append(total_score)

    total_scores.sort()

    mid_index = len(total_scores) // 2
    return total_scores[mid_index]


result = get_middle_autocomplete_score()
print(result)

