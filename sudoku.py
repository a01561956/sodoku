# sodoku


def txtToArray(file):
    sodoku_array = [[0]*9 for i in range(9)]
    file_txt = open(file)
    row = 0
    column = 0
    not_digit = True
    for line in file_txt:
        string = line.split()
        for i in string:
            if i == ".":
                sodoku_array[column][row] = 0
                row += 1
                not_digit = False
            elif not i.isdigit():
                not_digit = True
                continue
            else:
                sodoku_array[column][row] = int(i)
                row += 1
                not_digit = False
        if not_digit:
            row = 0
            continue
        else:
            column += 1
            row = 0
    return sodoku_array


def solve(sodoku_array):
    find = find_empty(sodoku_array)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(sodoku_array, i, (row, col)):
            sodoku_array[row][col] = i

            if solve(sodoku_array):
                return True

            sodoku_array[row][col] = 0

    return False


def valid(sodoku_array, num, pos):

    for i in range(len(sodoku_array[0])):
        if sodoku_array[pos[0]][i] == num and sodoku_array[1] != i:
            return False

    for i in range(len(sodoku_array)):
        if sodoku_array[i][pos[1]] == num and sodoku_array[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if sodoku_array[i][j] == num and (i, j) != pos:
                return False

    return True


def find_empty(sodoku_array):
    for i in range(len(sodoku_array)):
        for j in range(len(sodoku_array[0])):
            if sodoku_array[i][j] == 0:
                return (i, j)  # row, col

    return None


def printBoard(sodoku_array):
    for i in range(0, 9):
        for j in range(0, 9):
            print(sodoku_array[i][j], end=" ")
        print()


if __name__ == "__main__":
    # file = "sodoku.txt"
    # file = "sodoku_easy.txt"
    # file = "sodoku_mid.txt"
    # file = "sodoku_hard.txt"
    # file = "sodoku_evil.txt"
    # file = "sodoku_hardest.txt"
    array = txtToArray(file)
    solve(array)
    printBoard(array)
