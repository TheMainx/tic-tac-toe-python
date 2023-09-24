board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
turn = 0
for i in range(3):
    print(board[i])
def if_win():
    global board
    value = 0
    win = 0
    #checking if there are three the same chars in a row
    for val in range(-1, 3, 2):
        value = val
        for char in range(3):
            if board[char] == [value, value, value]:
                win = value
            #checking if there are three the same chars in a column
            elif board[0][char] == board[1][char] == board[2][char] == value:
               win = value
         #checking if there are three the same chars in a diagonal
        if board[0][0] == value and board[1][1] == value and board[2][2] == value:
            win = value
        elif board[0][2] == value and board[1][1] == value and board[2][0] == value:
            win = value
    #checking if board is full
    if 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
        print("Nobody win. Draw!")
        return 1
    #printing who win
    elif win:
        print("Player with ", win, ' win!')
    return win


while if_win() == False:
    if turn % 2 == 0:
        pos = list(map(int, input().split()))
        if board[pos[0]][pos[1]] != 0:
            print("Wrong move")
            turn += 1
        elif board[pos[0]][pos[1]] == 0:
            board[pos[0]][pos[1]] = 1
        for i in range(3):
            print(board[i])
    else:
        pos = list(map(int, input().split()))
        if board[pos[0]][pos[1]] != 0:
            print("Wrong move")
            turn += 1
        elif board[pos[0]][pos[1]] == 0:
            board[pos[0]][pos[1]] = -1
        for i in range(3):
            print(board[i])
    turn += 1
