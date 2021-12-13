import copy


def get_data():
    f = open('04_input.txt', 'r')
    data_str = f.read()
    data_str_split = data_str.split('\n')

    numbers_drawn = [int(number_str) for number_str in data_str_split[0].split(',')]

    bingo_grids = []

    grid = []
    counter = 0
    for i in range(1, len(data_str_split)):
        if not data_str_split[i]:
            continue
        counter += 1
        row = data_str_split[i].split(' ')
        tuple_row = [(int(column), False) for column in row if column]
        grid.append(tuple_row)

        if counter == 5:
            bingo_grids.append(copy.deepcopy(grid))
            del grid[:]
            grid = copy.deepcopy([])
            counter = 0

    return numbers_drawn, bingo_grids


def play_turn(bingo_grids, number_drawn):
    for grid in bingo_grids:
        for row in grid:
            for index, column_tuple in enumerate(row):
                if column_tuple[0] == number_drawn:
                    row[index] = (number_drawn, True)


def get_winner(bingo_grids):
    for grid_index, grid in enumerate(bingo_grids):
        for row in grid:
            num_seen_numbers = len([column_tuple for column_tuple in row if column_tuple[1]])
            if num_seen_numbers == 5:
                return grid

        for row_index in range(5):
            num_seen_numbers = len(
                [
                    grid[column_index][row_index] for
                    column_index in range(5) if
                    grid[column_index][row_index][1]
                ]
            )
            if num_seen_numbers == 5:
                return grid

    return None


# Part 1
def play_bingo():
    numbers_drawn, bingo_grids = get_data()

    for index, number in enumerate(numbers_drawn):
        play_turn(bingo_grids, number)

        if index >= 4:
            winner = get_winner(bingo_grids)
            if winner:
                unmarked_numbers = []
                for row in winner:
                    for col_tuple in row:
                        if not col_tuple[1]:
                            unmarked_numbers.append(col_tuple[0])

                final_score = number * sum(unmarked_numbers)
                return final_score


print(play_bingo())


# Part 2
def play_bingo_2():
    numbers_drawn, bingo_grids = get_data()

    last_winner = []
    winning_number = -1
    for index, number in enumerate(numbers_drawn):
        play_turn(bingo_grids, number)

        if index >= 4:
            winner = get_winner(bingo_grids)
            while winner:
                winning_number = number

                last_winner = copy.deepcopy(winner)
                bingo_grids.remove(winner)

                winner = get_winner(bingo_grids)

    unmarked_numbers = []
    for row in last_winner:
        for col_tuple in row:
            if not col_tuple[1]:
                unmarked_numbers.append(col_tuple[0])

    final_score = winning_number * sum(unmarked_numbers)
    return final_score


print(play_bingo_2())



