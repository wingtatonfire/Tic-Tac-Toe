from game_board import game_board_row, separation
import random


def pick_position():
    row_position = int(input("Please pick the position in row: "))
    column_position = int(input("Please pick the position in column: "))

    if row_position == 1:
        if column_position == 1:
            row_1[0] = "  X  "
            occupied_position.append((1, 1))
        if column_position == 2:
            row_1[2] = "  X  "
            occupied_position.append((1, 2))
        if column_position == 3:
            row_1[4] = "  X  "
            occupied_position.append((1, 3))

    if row_position == 2:
        if column_position == 1:
            row_2[0] = "  X  "
            occupied_position.append((2, 1))

        if column_position == 2:
            row_2[2] = "  X  "
            occupied_position.append((2, 2))

        if column_position == 3:
            row_2[4] = "  X  "
            occupied_position.append((2, 3))

    if row_position == 3:
        if column_position == 1:
            row_3[0] = "  X  "
            occupied_position.append((3, 1))

        if column_position == 2:
            row_3[2] = "  X  "
            occupied_position.append((3, 2))

        if column_position == 3:
            row_3[4] = "  X  "
            occupied_position.append((3, 3))

    return row_1, row_2, row_3, occupied_position


def display_gameboard():
    row_1_display = "".join(row_1)
    row_2_display = "".join(row_2)
    row_3_display = "".join(row_3)

    print(row_1_display + "\n" + separation + "\n" + row_2_display + "\n" + separation + "\n" + row_3_display)


def computer_turn():
    pass


def computer_pick():
    row_num = random.randint(1,3)
    column_num = random.randint(1,3)
    picked_position = (row_num, column_num)
    return picked_position


def computer_draw(position):
    row_position = position[0]
    column_position = position[1]
    if row_position == 1:
        if column_position == 1:
            row_1[0] = "  O  "
        if column_position == 2:
            row_1[2] = "  O  "
        if column_position == 3:
            row_1[4] = "  O  "

    if row_position == 2:
        if column_position == 1:
            row_2[0] = "  O  "

        if column_position == 2:
            row_2[2] = "  O  "

        if column_position == 3:
            row_2[4] = "  O  "

    if row_position == 3:
        if column_position == 1:
            row_3[0] = "  O  "

        if column_position == 2:
            row_3[2] = "  O  "

        if column_position == 3:
            row_3[4] = "  O  "

    return row_1, row_2, row_3, occupied_position_computer


def check_win():


occupied_position = []
occupied_position_computer = []
row_1 = game_board_row.copy()
row_2 = game_board_row.copy()
row_3 = game_board_row.copy()

while True:
    repeated = True
    pick_position()
    display_gameboard()
    while repeated:
        picked_position_by_computer = computer_pick()
        if picked_position_by_computer not in occupied_position:
            if picked_position_by_computer not in occupied_position_computer:
                computer_draw(picked_position_by_computer)
                occupied_position_computer.append(picked_position_by_computer)
                repeated = False
    display_gameboard()




