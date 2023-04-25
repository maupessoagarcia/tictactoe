def main():
    board = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
        ]

    active_player_index = 0
    players = ["You", "Computer"]
    symbols = ["X","O"]

    while not find_winner(board):
        player = players[active_player_index]
        announce_turn(player)
        show_board(board)
        input("pause")
        
def show_board(board):
    for line in board:
        string = f"| {line[0]} | {line[1]} | {line[2]} |"
        print(string)
        print("-"*len(string))

def announce_turn(player):
    print()
    print(f"It's {player}'s turn. Here's the board:")
    print()

def find_winner(board):
    return False


if __name__ == "__main__":
    main()
