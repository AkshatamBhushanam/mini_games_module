import random

class GuessNumber:

    def __init__(self):
        self.main()

    def compare(self, user, number):
        if user < number:
            print("Guess higher")
            return False
        
        elif user > number:
            print("Guess lower")
            return False
        
        elif user == number:
            print("You have successfully guessed the number")
            return True
        

    def main(self):
        user = -1
        n_guesses = 0
        number = random.randint(0, 100)
        while user != number:
            n_guesses += 1
            try:
                user = int(input("Guess the number: "))
                self.compare(user, number)
            except Exception as e:
                print(e)

        print(f"You guessed the number in {n_guesses} guessed")


if __name__ == "__main__":
    game = GuessNumber()

