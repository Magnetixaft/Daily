# Given a list of building in the form of (left, right, height), return what the skyline should look like. The skyline should be in the form of a list of
# (x-axis, height), where x-axis is the next point where there is a change in height starting from 0, and height is the new height starting from the x-axis.
# Print out
import numpy as np
changes_cords = []
def generate_skyline(buildings):
    num_changes = len(buildings)
    max_height = 0
    width = 9
    change_in_height = 0
    for i in range(len(buildings)):
        poss_max = buildings[i][2]
        if poss_max > max_height:
            max_height = poss_max
    field = np.full((max_height, width), 0)
    def change_value(left, right, up, times):
        for k in range(max_height - 1, max_height - up - 1, -1):

            for j in range(left - 1, right):
                field[k][j] = times
        return field

    def get_cord(cord):
        global start, height, end
        start = buildings[cord][0]
        end = buildings[cord][1]
        height = buildings[cord][2]
        return start, end, height

    for j in range(len(buildings)):
        get_cord(j)
        change_in_height += 1
        change_value(start, end, height, change_in_height)
    print(field)

    # Sloppy, but works
    def cords_of_change(board):
        for p in range(width):

            for z in range(0, len(board)):
                if board[z][p] == 0:
                    continue
                if board[z][p] != 0 and len(changes_cords) == 0:
                    changes_cords.append(p + 1)
                    changes_cords.append(len(board) - z)
                    break
                if board[z][p] != 0 and changes_cords[len(changes_cords) - 1] != (len(board) - z):
                    changes_cords.append(p + 1)
                    changes_cords.append(len(board) - z)
                    break
                break
        return changes_cords

    cords_of_change(field)
    print(changes_cords)


generate_skyline([(2, 8, 3), (4, 6, 5)])
