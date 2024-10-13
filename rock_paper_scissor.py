import random
class RockPaperScissor:
    
    # typical game of rock paper scissor, first to 10 points wins!
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.main()

    def gameWin(self, comp, user):
        # return 0 -> user, 1 -> comp, 2 -> tie 

        if user == comp:
            print("Its a Tie")
            return 2
        
        elif (user == "rock" and comp == "paper") or (user == "paper" and comp == "scissor") or (user == "scissor" and comp == "rock"):
            print("Computer score")
            return 1

        elif (user == "rock" and comp == "scissor") or (user == "paper" and comp == "rock") or (user == "scissor" and comp == "paper"):
            print(f"You score")
            return 0
        
        else:
            print("wrong input")
            return 2

                
    def main(self):
        user = ""
        u_score = 0
        c_score = 0
        choice = ["rock", "paper", "scissor"]
        while u_score < 10 and c_score < 10:
            comp = random.choice(choice)
            print(f"\nYour score: {u_score}, Computer Score: {c_score}")
            user = input("rock, paper or scissor?: ").lower()
            winner = self.gameWin(comp, user)
            if winner == 0:
                u_score += 1
            elif winner == 1:
                c_score += 1
            
        if u_score == 10:
            print("Congratulations You won!\n")
        else:
            print("The computer has won!\n")

if __name__ == "__main__":
    game = RockPaperScissor("Akshat", "ChatGPT")