from game_board import game_board_row, separation
import random
from winning_condition import win_conditions


def pick_position(occupied_position, occupied_position_computer):
    while True:
        row_position = int(input("Please pick the position in row: "))
        column_position = int(input("Please pick the position in column: "))
        if 0 < row_position < 4 and 0 < column_position < 4:
            picked_position = (row_position, column_position)
            while picked_position in occupied_position or picked_position in occupied_position_computer:
                print("Spot is occupied. Please pick another spot.")
                row_position = int(input("Please pick the position in row: "))
                column_position = int(input("Please pick the position in column: "))
                picked_position = (row_position, column_position)

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

        else:
            print("The number you pick is out of range")


def display_gameboard():
    row_1_display = "".join(row_1)
    row_2_display = "".join(row_2)
    row_3_display = "".join(row_3)

    print(row_1_display + "\n" + separation + "\n" + row_2_display + "\n" + separation + "\n" + row_3_display)


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


def check_win(win_condition, placement, player):
    is_on = True
    for condition in win_condition:
        if not is_on:
            return False
        win = 0
        for spot in condition:
            if spot in placement:
                win += 1
                if win == 3:
                    print(f"{player} Win")
                    is_on = False
    return True


occupied_position = []
occupied_position_computer = []
game_is_on = True
row_1 = game_board_row.copy()
row_2 = game_board_row.copy()
row_3 = game_board_row.copy()
counter = 0

while game_is_on:
    repeated = True
    pick_position(occupied_position, occupied_position_computer)
    counter += 1
    display_gameboard()
    game_is_on = check_win(win_conditions, occupied_position, "Player")
    if counter == 9:
        game_is_on = False
        print("Draw")
    while repeated and game_is_on:
        picked_position_by_computer = computer_pick()
        if picked_position_by_computer not in occupied_position:
            if picked_position_by_computer not in occupied_position_computer:
                computer_draw(picked_position_by_computer)
                counter += 1
                occupied_position_computer.append(picked_position_by_computer)
                repeated = False
                game_is_on = check_win(win_conditions, occupied_position_computer, "Computer")

    display_gameboard()
print("GG")




