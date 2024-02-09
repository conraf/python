import random

def play_game():
    
    choices = ["rock", "paper", "scissors"]
    print("Welcome to Rock-Paper-Scissors Game!")

    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Your turn, enter 'rock', 'paper' or 'scissors': ").lower()
        if player_choice not in choices:
            print("Invalid choice! Please choose 'rock', 'paper' or 'scissors'.")
            continue

        computer_choice = random.choice(choices)
        print("Computer's turn, computer chose: {}".format(computer_choice))

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print("Score:\nPlayer: {} - Computer: {}".format(player_score, computer_score))

        play_again = input("\nDo you want to play again? (y/n) ").lower()
        if play_again != "y":
            break

if __name__ == "__main__":
    play_game()
