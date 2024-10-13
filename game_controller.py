import rock_paper_scissor as rps
import memorize as memo
import tic_tac_toe as tic
import guess_number as gn
import hangman as hg

class GameController:

    def __init__(self):
        self.player1 = input("Please enter the name of the player1: ")
        self.player2 = input("Please enter the name of the player2: ")
        
        print("\nWelcome to our Game module!")
        print("write the name of the game you want to play -")
        print("We have games such as RockPaperScissor, Hangman, TicTacToe, memorize and Guess the Number")
        self.play(self.player1, self.player2)

    
    def play(self, player1, player2):
        user_choice = None

        while user_choice != "no":
            print("RockPaperScissor, hangman, TicTacToe, memorize, GuessTheNumber")
            user_choice = input("Which game you want to play now?: ").lower()
            user_choice = user_choice.replace(" ", "")
            
            if "rockpaper" in user_choice:
                rps.RockPaperScissor(player1, player2)

            elif "tictac" in user_choice:
                tic.TicTacToe(player1, player2)

            elif "memo" in user_choice:
                memo.Memorize()

            elif "guess" in user_choice:
                gn.GuessNumber()

            elif "hangman" in user_choice:
                hg.Hangman()

            elif "exit" in user_choice:
                exit()


if __name__ == "__main__":
    gameplay = GameController()