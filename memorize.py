import os
import random
import time

def clear_screen():
    # Clear the terminal screen based on the operating system
    if os.name == "nt":
        os.system('cls')
    else:               # For MacOS/Linux
        os.system('clear')

class Memorize:

    def __init__(self):
        self.main()
        print("Thanks for playing this game")

    def main(self):
        random_nos = []
        guess_list = []
        failed = False
        no_number = 1
        
        while not failed:

            guess_list.clear()

            input("Get Ready! Press enter to start...")
            random_nos.append(random.randint(0, 100))
            for number in random_nos:
                print(number)
            
            time.sleep(5)
            print("The screen is about to clear")
            clear_screen()
            
            print("Now guess the numbers which were displayed-")
            
            for i in range(no_number):
                try:
                    guess = int(input(f"The {i+1} number was: "))
                    guess_list.append(guess)

                except Exception as e:
                    print(e)

            if random_nos == guess_list:
                print("You successfully guessed the nos.\n")

            else:
                print("Your guess was wrong!")
                print(random_nos)
                failed = True

            no_number +=1

if __name__ == "__main__":                
    game = Memorize()
