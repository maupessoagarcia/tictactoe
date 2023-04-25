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
        announce_turn(player)
        show_board(board)
        print()
        input("pause")
        
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
