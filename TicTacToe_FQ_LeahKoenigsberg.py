#create a tic tac toe board:

#variables for scoreboard
player_wins = 0
player2_wins = 0
tie = 0


#define main function
def main():
  global player_wins, player2_wins, tie
  #while user enters y for yes replay the game
  again = 'y'
  while again.lower() == 'y':
    #create a 2 dimensional list with rows and columns
    board = []
    row,col = 3, 3
    for r in range(row):
        rows = []
        for c in range(col):
            rows.append('-')
        #append to make an entire board
        board.append(rows)

    #call function to play
    player_wins, player2_wins, tie = player(board, player_wins, player2_wins, tie)
    
    #print scoreboard after each game
    print('\n               Scoreboard:')
    print('--------------------------')
    print('\nPlayer 1 wins: ',player_wins)
    print('Player 2 wins: ',player2_wins)
    print('Number of ties: ',tie)

    #ask user if would like to replay
    again = input('\nWould you like to play again? (y for yes) ')

#function that prints board neatly
def print_board(board):
    print('  0 1 2')
    #nested for loop that loops through each element to print
    for r in range(len(board)):
        print(r, end=' ')
        for c in range(len(board[r])):
            print(board[r][c], end = ' ')
        print()
    
  
#function to play game
def player(board, player_wins, player2_wins, tie):
  
  #variables keep score
  taken = 0
  game = 0
  comma = ','
  print('Welcome to the Tic Tac Toe Challenge!')

  #while game board is not full or no player got a row:
  while taken != 9 and game != 1:
    
    #two players loop through giving each a turn
    for i in ['one','two']:
        print()
        #print board so player can find coordinates
        print_board(board)

        #call function to validate input
        tpl = validate_input(board, i)

        #change the '-' on the board to 'X' or 'O' in the spot the user chose
        if i == 'one':
          board[tpl[0]][tpl[1]] = 'X'
        else:
          board[tpl[0]][tpl[1]] = 'O'

        #keep count of number of spots left on board
        taken +=1

        #call function to determine if player won
        game, player_wins, player2_wins, tie = win_game(board, taken, player_wins, player2_wins, tie)

        #if player one then end game
        if game == 1:
          break

          
  #return variables
  return player_wins, player2_wins, tie

#input validation function
def validate_input(board, i):
  comma = ','
  
  print('\nPlayer',i,': \nPlease enter a number from 0 to 2 for a row and column: ',end = '')
  rws_cols = input('(Hint: row #, comma and then the column #) ')
  rw = rws_cols.split(",")
  cls = rw[0]
  rws = rw[1]

  #call function to change 
  tpl = change_int(rws,cls)

  #Input validation: if user enters one number or doesnt put a comma:
  while comma not in rws_cols or len(rws_cols) > 4 or tpl[0] > 2 or tpl[0] < 0 or tpl[1] > 2 or tpl[1] < 0 or board[tpl[0]][tpl[1]] == 'X' or board[tpl[0]][tpl[1]] == 'O':
    #if input is greater than 2 or less than 0
    if comma not in rws_cols or len(rws_cols) > 4 or tpl[0] > 2 or tpl[0] < 0 or tpl[1] >2 or tpl[1] <0:
      print('\nInput must be two numbers from 0-2 separated by a comma.')
      
    #spot on board taken
    else:
      print('\nThis spot is already taken.')

    #ask user for new coordinates
    rws_cols = input('Enter a number from 0-2 for a row and column separated by a comma: (Hint: row #, comma and then the column #) ')     

    #split users answer by the comma
    rw = rws_cols.split(",")
    cls = rw[0]
    rws = rw[1]

    #call function to change 
    tpl = change_int(rws,cls)

  return tpl   

#function that changes to integer
def change_int(rws,cls):
  try:
    #create a tuple with the row and column user entered
    tpl = (int(rws), int(cls))
    return tpl
  except ValueError:
    print('Error.')
  
#function to determine if player won game
def win_game(board, taken, player_wins, player2_wins, tie):

  #variables
  row1 = 0
  row2 = 0
  col1 = 0
  col2 = 0
  game = 0

  #loop through nested loop to determine 'X' and 'O'
  for i in range(len(board)):
    for j in range(len(board[i])):

      #if 'X' count how many in a row, accumulate variable
      if board[i][j] == 'X':
        row1+=1

      #if 'O' count how many in a row, accumulate variable
      if board[i][j] == 'O':
        row2+=1

      #if 'X' count how many in a column, accumulate variable
      if board[j][i] == 'X':
        col1+=1

      #if 'O' count how many in a column, accumulate variable
      if board[j][i] == 'O':
        col2+=1

    #if 'X' count is 3 in a row then player one won!
    if row1 == 3 or col1 == 3:
      print('\nCongrats player 1- you got a row!')
      #print board to show results
      print_board(board)
      #add to scoreboard
      player_wins += 1
      game = 1

    #if 'O' count is 3 in a row then player two won!
    if row2 == 3 or col2 == 3:
      print('\nCongrats player 2- you got a row!')
      print_board(board)
      player2_wins += 1
      game = 1


    #put variables down to 0
    row1 = 0
    row2 = 0
    col1 = 0
    col2 = 0

  #if 'X' is found in all three places, player one got a row diagonally!
  if (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') or (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):
    print('\nCongrats player 1- you got a row!')
    print_board(board)
    player_wins += 1
    game = 1
    
  #if 'O' is found in all three places, player two got a row diagonally!
  if (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') or (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
    print('\nCongrats player 2- you got a row!')
    print_board(board)
    player2_wins += 1
    game = 1


  #if board is full = tie
  if taken == 9 and game !=1:
    print('\nOh well, the board is full. You did not get a row.')
    print_board(board)
    tie += 1
    game = 1
    
  #return variables so can keep accurate scroe
  return game, player_wins, player2_wins, tie

#call to function main
main()
