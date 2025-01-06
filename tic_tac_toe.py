
class TicTacToe:

    def __init__ (self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = self.create_board()
        print("Wlecome to TicTacToe!")
        mode = input("Choose mode (2player/ai): ").lower()
        if mode == "2player":
            self.two_player_mode()
        elif mode == "ai":
            self.player2 = "AI"
            self.ai_mode()
            

    def create_board(self):
        return [" "]*9

    def show_board(self, board):
        print("\n")
        for i in range(0, 9, 3):
            print(f"{board[i]}  |  {board[i+1]}  |  {board[i+2]}")
            if i < 6:
                print("--------------")
        print("\n")

    def check_winner(self, board):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  
            (0, 4, 8), (2, 4, 6)              
        ]
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != " ":
                winner = self.player1 if board[combo[0]] == "X" else self.player2
                return [True, winner]
        if self.check_tie(board):
            return [True, "No one"]
        return [False, ""]
              
    def check_tie(self, board):
        for box in board:
            if box == " ":
                return False
        return True

    def minimax(self, depth, is_maximizing, minimax_board):
        result = self.check_winner(minimax_board)
        if result[0]:
            if result[1] == self.player2:
                return 10 - depth  
            elif result[1] == self.player1:
                return depth - 10  
            else:
                return 0  

        if is_maximizing:
            best_score = -1000
            for i in range(9):
                if minimax_board[i] == " ":
                    minimax_board[i] = "O"
                    score = self.minimax(depth + 1, False, minimax_board)
                    minimax_board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = 1000
            for i in range(9):
                if minimax_board[i] == " ":
                    minimax_board[i] = "X"
                    score = self.minimax(depth + 1, True, minimax_board)
                    minimax_board[i] = " "
                    best_score = min(score, best_score)
            return best_score

    def find_best_move(self, board):
        best_move = -1
        best_score = -1000
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = self.minimax(0, False, board)
                board[i] = " "
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move


    def two_player_mode(self):
        self.create_board()
        curr_player = self.player1
        print("Get ready for TicTacToe!")
        input("Press enter to continue...")

        while True:
            self.show_board(self.board)
            print(f"{curr_player}'s Turn")
            try:
                move = int(input("Enter your move (0-8): "))
                if self.board[move] == " ":
                    self.board[move] = "X" if curr_player == self.player1 else "O"
                    curr_player = self.player2 if curr_player == self.player1 else self.player1
            
                else:
                    print("Invalid move! Try again")
            except Exception as e:
                print(e)
            
            if self.check_winner(self.board)[0]:
                self.show_board(self.board)
                print(f"{self.check_winner(self.board)[1]} wins!")
                break

    def ai_mode(self):
        self.create_board()
        curr_player = self.player1
        print("Get ready for TicTacToe!")
        input("Press enter to continue...")

        while True:
            self.show_board(self.board)
            print(f"{curr_player}'s Turn")

            if curr_player == self.player1:
                try:
                    move = int(input("Enter your move (0-8): "))
                    if self.board[move] == " ":
                        self.board[move] = "X"
                        curr_player = self.player2
                    else:
                        print("Invalid move! Try again")
                except Exception as e:
                    print(e)

                

            elif curr_player == self.player2:
                move = self.find_best_move(self.board)
                if self.board[move] == " ":
                    self.board[move] = "O"
                    curr_player = self.player1

            if self.check_winner(self.board)[0]:
                self.show_board(self.board)
                print(f"{self.check_winner(self.board)[1]} wins!")
                break
      


if __name__ == "__main__":
    TicTacToe("Askhat", "Jyotsna")
