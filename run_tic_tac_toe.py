from board import Board

GAME_STATE = {
              'running' : 0,
              'win'   : 1,
              'draw'    : 3,
              }

def tic_tac_toe_game(size = 3):

  board = Board(size,size)

  while check_game(board) == GAME_STATE['running']:

    # print board
    print(board)

    # ask for input 
    in_str = input("Next Move? x,y,sym\n")

    in_list = in_str.strip().split(",")
    
    x = int(in_list[0])
    y = int(in_list[1])
    sym = in_list[2]

    # update game state
    board.change_cell(x,y,sym)

  print(board)

  game_state = check_game(board)
  if game_state == GAME_STATE['draw']:
    print("Game was a draw")
  elif game_state == GAME_STATE['win']:
    print("Someone Won!")
  else:
    print("I don't know how we got here?")

def check_win(board):

  # check rows 
  for row in board.game_board:
    
    row_equal = True
    cell_0 = row[0].val

    if cell_0 == " ":
      continue
    
    for cell in row[1:]:
      row_equal &= (cell_0 == cell.val)

    if row_equal:
      return True

  # check cols
  for ix in range(board.Nx):
    
    col_equal = True
    cell_0 = board.game_board[0][ix].val

    if cell_0 == " ":
      continue

    for iy in range(1,board.Ny):
      cell = board.game_board[iy][ix]
      col_equal &= (cell_0 == cell.val)

    if col_equal:
      return True

  # check diagonals
  diag_equal = True
  cell_0 = board.game_board[0][0].val

  if cell_0 != " ":

    for idx in range(1, board.Nx):
      cell = board.game_board[idx][idx]
      diag_equal &= (cell_0 == cell.val)

    if diag_equal:
      return True

  # check diagonals
  diag_equal = True
  cell_0 = board.game_board[0][board.Nx-1].val

  if cell_0 != " ":

    for idx in range(1, board.Nx):
      cell = board.game_board[idx][board.Nx-1-idx]
      diag_equal &= (cell_0 == cell.val)

    if diag_equal:
      return True

  return False

def check_draw(board):

  for row in board.game_board:
    for cell in row:

      if cell.val == " ":
        return False

  return True

def check_game(board):

  if check_win(board):
    return GAME_STATE['win']
  
  if check_draw(board):
    return GAME_STATE['draw']

  return GAME_STATE['running']


def run():
  tic_tac_toe_game()

if __name__ == "__main__":
    run()
