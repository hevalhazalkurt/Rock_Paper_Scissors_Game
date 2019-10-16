import time
import random


rock = 1
paper = 2
scissors = 3


names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules = {rock: scissors, paper: rock, scissors: paper}


player_score = 0
computer_score = 0


def start():
    print("")
    print("Ready for a game of Rock, Paper, Scissors?")
    while game():
        pass
    scores()



def game():
    player = move()
    computer = random.randint(1,3)
    result(player, computer)
    return play_again()



def move():
    while True:
        print("")
        player = input("""
        Rock = 1
        Paper = 2
        Scissors = 3

        Make a move : """)

        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print("I didn't understand that. Please enter 1, 2 or 3.")



def result(player, computer):
    print("")
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3!")
    time.sleep(0.5)
    print("")

    print("Computer threw {}!".format(names[computer]))
    global player_score, computer_score

    if player == computer:
        print("Tie game.")
    else:
        if rules[player] == computer:
            print("Your victory has been assured.")
            player_score += 1
        else:
            print("The computer laughs as you realise you have been defeated.")
            computer_score += 1



def play_again():
    print("")
    answer = input("Would you like to play again? y/n: ")
    if answer in ("y", "yes", "Yes", "YES", "Of course!", "of course"):
        return answer
    else:
        print("Thank you for playing my game. See you next time!")



def scores():
    global player_score, computer_score
    print("")
    print("HIGH SCORES")
    print("Player: ", player_score)
    print("Computer: ", computer_score)


if __name__ == "__main__":
    start()
