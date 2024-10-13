import random

class Hangman:

    words = ["aarav", "vivaan", "aditya", "vihaan", "parth", "krishna", "dev", 
    "rahul", "rohit", "aman", "harsh", "ananya", "karan", "ritesh", 
    "siddharth", "ishaaan", "shreyas", "yash", "manish", "ankit", 
    "kushal", "suryansh", "ashwin", "nishant", "tejas", "abhay", 
    "rishabh", "ankur", "puneet", "neeraj", "gagan", "sahil"]

    def __init__(self):
        self.main()
    
    def isGuessed(self, guess_list):
        for i in guess_list:
            if i == "_":
                return False
        
        return True
    
    def updateGuessList(self, guess_list, word, user):
        for i, letter in enumerate(word, start=0):
            if user == letter:
                guess_list[i] = user
                

        return guess_list 
        
    def main(self):

        word = random.choice(Hangman.words)
        guess_list = ["_"] * len(word)
        hint_index = random.randint(0, len(word) - 1)
        guess_list[hint_index] = word[hint_index]
        guesses_left = 2 * len(word)

        print("Try to guess the common names of Indian boys")
        input("Press enter to continue...")
        user = None

        while not self.isGuessed(guess_list):

            if guesses_left == 0:
                    print("You have no guessed left")
                    print(f"The word was {word}")
                    break
            
            try:
                print(" ".join(guess_list))
                print(f"Chances left: {guesses_left}")
                user = input("Guess the word: ").lower()
                if user in word:
                    guess_list = self.updateGuessList(guess_list, word, user)

                else:
                    print("Wrong guess")
                    guesses_left -= 1


                if self.isGuessed(guess_list):
                    print("You have guessed the word correctly!")
                    print(word)
                    break

            except Exception as e:
                print(e)


if __name__ == "__main__":
    game = Hangman()
    
