
class TicTacToe:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        print("You have to enter the number of your block(0-8),eg - 6 for the block in bottom most left ")
        self.main()


    def createBoard(self):

        self.board = []
        self.win_cords = ["", "", ""]
        
        for i in range(0, 9):
            self.board.append(" ")

    def showBoard(self, board):

        for i in range(0, 9, 3):
            print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
            print("----------")

    def checkDiagonal(self, board):
        if board[0] == board[4] and board[0] == board[8] and board[0] != " ":
            self.win_cords = [0, 4, 8]
            return True

        elif board[2] == board[4] and board[2] == board[6] and board[2] != " ":
            self.win_cords = [2, 4, 6]
            return True
        
        else:
            return False
        
    def checkVertical(self, board):
        for i in range(0, 3):
            if board[i] == board[i+3] and board[i] == board[i+6] and board[i] != " ":
                self.win_cords = [i, i+3, i+6]
                return True
        return False
            
    def checkHorizontal(self, board):
        for i in range(0, 7, 3):
            if board[i] == board[i+1] and board[i] == board[i+2] and board[i] != " ":
                self.win_cords = [i, i+1, i+2]
                return True
        return False
    
    def isTied(self, board):
        for i in range(0, 9):
            if board[i] == " ":
                return False
            
        return True


    def gameWin(self, board):
        if(self.checkDiagonal(board) or self.checkVertical(board) or self.checkHorizontal(board)):
            print(self.win_cords)
            print(f"{self.player1 if board[self.win_cords[0]] == "X" else self.player2} Wins!")
            return True
        
        
        elif(self.isTied(board)):
            print("The game is tied!")
            return True
        
        return False

    def main(self):

        isPlayer1Turn = True
        self.createBoard()

        print("Get ready")
        input("Press enter to continue...")
        while(not self.gameWin(self.board)):
            print("\n")
            curr_turn = "X" if isPlayer1Turn else "O"
            self.showBoard(self.board)
            print(f"{self.player1 if isPlayer1Turn else self.player2}({curr_turn})'s Turn")
            try:
                move = int(input("Enter the position of your move: "))

                if self.board[move] == " ":
                    self.board[move] = curr_turn

                    isPlayer1Turn = not isPlayer1Turn

                
            
            except Exception as e:
                print(e)

if __name__ == "__main__":
    game = TicTacToe()