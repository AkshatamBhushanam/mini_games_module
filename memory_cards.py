import random
import time
import os
class MemoryCardsGame:
    cards = []
    flipped_cards = []

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.cards = ["apple", "apple", "grapes", "grapes", "sweet berry", "sweet berry", "banana", "banana", "watermelon", "watermelon", "orange", "orange", "avocado", "avocado", "lemon", "lemon"]
        random.shuffle(self.cards)
        self.play()
    
    def clear_screen(self):
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def showCards(self, cardios):
        width = 4
        for i in range(0, len(cardios), width):
            print("    ".join(cardios[i:i+width]))

        time.sleep(1)

    def isGameOver(self, cardios):
        for item in cardios:
            if "*" in item:
                return False
            
        return True
    
    def flipCard(self, choices, cardios):
        temp_list = cardios[:]
        for i in choices:
            temp_list[i] = self.cards[i]
        self.showCards(temp_list)
        time.sleep(2)

    def checkPair(self, user1, user2):
        if(self.cards[user1] == self.cards[user2] and self.cards[user1] != " "):
            self.flipped_cards[user1] = " "
            self.flipped_cards[user2] = " "
            self.cards[user1] = " "
            self.cards[user2] = " "
            return True
        
        else:
            return False

    def play(self):
        scores = {self.player1: 0, self.player2: 0}
        self.flipped_cards = [f"*{index}" for index in range(0, len(self.cards))]
        isPlayer1Turn = True

        while(not self.isGameOver(self.flipped_cards)):
            print("\n")
            self.showCards(self.flipped_cards)
            curr_turn = self.player1 if isPlayer1Turn else self.player2
            
            try:
                print(f"\n{self.player1}'s score: {scores.get(self.player1)}, {self.player2}'s score: {scores.get(self.player2)}")
                print(f"Current Turn: {curr_turn}")
                choice1 = int(input("\nEnter your first flip: "))
                self.flipCard([choice1], self.flipped_cards)
                choice2 = int(input("\nEnter your second flip: "))
                self.flipCard([choice1, choice2], self.flipped_cards)
                self.clear_screen()
                matched = self.checkPair(choice1, choice2)
                if matched:
                    scores[curr_turn] += 1
                
                else:
                    isPlayer1Turn = not isPlayer1Turn

            except Exception as e:
                print(e)

        if scores.get(self.player1) > scores.get(self.player2):
            print(f"{self.player1} wins the game")
        else:
            print(f"{self.player2} wins the game")

if __name__ == "__main__":
    game = MemoryCardsGame("Akshat", "Jyotsna")


        
