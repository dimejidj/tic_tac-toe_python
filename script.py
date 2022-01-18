#Game Board Display
gameBoardObj = {1: " ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "}
from IPython.display import clear_output
def gameDisplay():
    print('\n'*100)

    row1 = [gameBoardObj[1] + ' || ' + gameBoardObj[2] + ' || ' + gameBoardObj[3]]
    row2 = [gameBoardObj[4] + ' || ' + gameBoardObj[5] + ' || ' + gameBoardObj[6]]
    row3 = [gameBoardObj[7] + ' || ' + gameBoardObj[8] + ' || ' + gameBoardObj[9]]
    
    print(row3)
    print('---------------')
    print(row2)
    print('---------------')
    print(row1)

    return row1, row2, row3

def weaponClickP1():
    weapons = ['X', 'O', 'x', 'o']
    player1Pick = 'ERROR'
    player2Pick = ''
    
    while player1Pick not in weapons:
        player1Pick = (input('Player 1 Pick a marker, X or O'))
    
    if player1Pick == 'X' or player1Pick == 'x':
        player2Pick = 'O'
    elif(player1Pick == 'O' or player1Pick == 'o'):
        player2Pick = 'X'
        
    print(f'player 1 Marker is {player1Pick}\nPlayer 2 Marker is {player2Pick}')
    
     
    return (player1Pick.upper(), player2Pick.upper())

player1Pick, player2Pick = weaponClickP1()



# check Play and Display it
gameOn = True
playerOneMove = True
playerTwoMove = False
count = 0

while gameOn == True and count < 10: 
    if(count == 9):
        print('===========')
        print('Draw Game - re-run code to play again')
        gameOn = False
        break
        
    def checkPlay():
        gameBoardNum = [1,2,3,4,5,6,7,8,9]
        playerPlay = 25
        while playerPlay not in gameBoardNum or gameBoardObj[playerPlay] != ' ':
            playerPlay = int(input('Select Position to play in between (1-9)'))
        return playerPlay

    playerMoveNow = checkPlay()

    def showPlayOnBoard(play):
        global playerOneMove
        global playerTwoMove

        if(playerOneMove == True):
            gameBoardObj[play] = player1Pick
            playerOneMove = False
        elif(playerOneMove == False):
            gameBoardObj[play] = player2Pick
            playerOneMove = True

        gameDisplay()
        return gameBoardObj

    showPlayOnBoard(playerMoveNow)
    
    def checkWinner():
        global gameOn
        global count
        if(gameBoardObj[1] == gameBoardObj[2] == gameBoardObj[3] and gameBoardObj[1] != ' '):
            print('===========')
            print(f'Winner is {gameBoardObj[1]}')
            gameOn = False
        if(gameBoardObj[4] == gameBoardObj[5] == gameBoardObj[6] and gameBoardObj[4] != ' '):
            print('===========')
            print(f'Winner is {gameBoardObj[1]}')
            gameOn = False
        if(gameBoardObj[7] == gameBoardObj[8] == gameBoardObj[9] and gameBoardObj[7] != ' '):
            print('===========')
            print(f'Winner is {gameBoardObj[7]}')
            gameOn = False
        if(gameBoardObj[1] == gameBoardObj[5] == gameBoardObj[9] and gameBoardObj[1] != ' '):
            print('===========')
            print(f'Winner is {gameBoardObj[1]}')
            gameOn = False
        if(gameBoardObj[3] == gameBoardObj[5] == gameBoardObj[7] and gameBoardObj[3] != ' '):
            print('===========')
            print(f'Winner is {gameBoardObj[3]}')
            gameOn = False
        if(gameBoardObj[1] == gameBoardObj[4] == gameBoardObj[7] and gameBoardObj[1] != ' '):
            print('===========')
            print(f'Winner is {gameBoardObj[1]}')
            gameOn = False
        if(gameBoardObj[2] == gameBoardObj[5] == gameBoardObj[8] and gameBoardObj[2] != ' '):
            print('===========')
            print(f'Winner is {gameBoardObj[7]}')
            gameOn = False
        if(gameBoardObj[3] == gameBoardObj[6] == gameBoardObj[9] and gameBoardObj[3] != ' '):
            print('===========')
            print(f'Winner is {gameBoardObj[3]}')
            
            gameOn = False
        return gameOn
    
    checkWinner()
    count += 1