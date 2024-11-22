def checkmate(board):
    
    board = board.strip().split('\n')
    size = len(board)
    
        king_pos = None
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break
    
    if not king_pos:
        print("Error: No King found on the board.")
        return

    directions = {
        'P': [(-1, -1), (-1, 1)],
        'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],
        'R': [(-1, 0), (1, 0), (0, -1), (0, 1)],
        'Q': [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)],
    }
    
  
    for i in range(size):
        for j in range(size):
            piece = board[i][j]
            if piece in directions:
                for direction in directions[piece]:
                    x, y = i, j
                    while 0 <= x < size and 0 <= y < size:
                        x += direction[0]
                        y += direction[1]
                        if not (0 <= x < size and 0 <= y < size):
                            break
                        if (x, y) == king_pos:
                            print("Success")
                            return
                        if board[x][y] != '.':
                            break

    print("Fail")


def main():
    
    boards = [
        """\
R...
.K..
..P.
....\
""",   

        """\
....
.K..
.P..
....\
""",  

        """\
....
..B.
....
.K..\
""",  

        """\
....Q
......
......
...K..\
""",  

        """\
..
.K\
""",  

        """\
........
...B....
........
........
....K...
........
...P....
........\
""",  
    ]

    
    for idx, board in enumerate(boards, 1):
        print(f"Board {idx}:")
        checkmate(board)
        print()


if __name__ == "__main__":
    main()
