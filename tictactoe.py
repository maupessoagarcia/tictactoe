def main():
    board = [
        [None,None,None],
        [None,None,None],
        [None,None,None]
        ]

    active_player_index = 0
    players = ["You", "Computer"]
    symbols = ["X","O"]

    while not find_winner(board):
        player = players[active_player_index]
        symbol = symbols[active_player_index]
        announce_turn(player)
        show_board(board)
        if not choose_location(board, symbol):
            print("That isn't an option, try again.")
            continue
        print()
        input("pause")


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
    return False


if __name__ == "__main__":
    main()
