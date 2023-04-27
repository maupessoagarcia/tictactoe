def main():
    board = [
        [None,None,None],
        [None,None,None],
        [None,None,None]
        ]

    active_player_index = 0
    players = ["You", "Computer"]
    symbols = ["X","O"]
    player = players[active_player_index]

    while not find_winner(board):
        if full_board(board):
            print(f"Game over! It was a tie, with this board: ")
            print()
            show_board(board)
            print()
            break
        player = players[active_player_index]
        symbol = symbols[active_player_index]
        announce_turn(player)
        show_board(board)
        print()
        if not choose_location(board, symbol):
            print("That isn't an option, try again.")
            continue
        print()
        active_player_index = (active_player_index + 1)% len(players)
        if find_winner(board):
    
            print(f"Game over! {player} has won with the board: ")
            print()
            show_board(board)
            print()


def choose_location(board,symbol):
    row = int(input("Choose which row: "))
    column = int(input("Choose which column: "))

    row -=1
    column-=1
    if row<0 or row>= len(board):
        return False
    if column<0 or column>= len(board[0]):
        return False
    

    cell = board[row][column]
    if cell is not None: 
        return False

    board[row][column] = symbol
    return True

        
def show_board(board):
    for line in board:
        print("| ", end="")
        for cell in line:
            symbol = cell if cell is not None else "_"
            print(symbol, end=" | ")
        print()

def announce_turn(player):
    print()
    print(f"It's {player}'s turn. Here's the board:")
    print()

def find_winner(board):
    sequences = get_winning_sequences(board)

    for cells in sequences:
        symbol1 = cells[0]
        if symbol1 and all(symbol1 == cell for cell in cells):
            return True

    return False
    

def get_winning_sequences(board):
    sequences = []
    #rows
    sequences.extend(board)

    #columns

    for ind in range(0,3):
        sequences.append([board[0][ind],board[1][ind],board[2][ind]])

    #diagonals

    diag = [[board[0][0],board[1][1],board[2][2]],[board[0][2],board[1][2],board[2][0]]]
    sequences.extend(diag)

    return sequences

def full_board(board):
    for row in board:
        for cell in row:
            if cell == None:
                return False
    return True


if __name__ == "__main__":
    main()


#IMPLEMENT NO WINNER LOGIC