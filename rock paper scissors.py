def get_player_choice(player_name):
    while True:
        choice = input(f"{player_name}, please enter your choice (rock, paper, scissors): ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "It's a tie!"
    elif (choice1 == 'rock' and choice2 == 'scissors') or \
         (choice1 == 'scissors' and choice2 == 'paper') or \
         (choice1 == 'paper' and choice2 == 'rock'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def play_round(player1_name, player2_name):
    choice1 = get_player_choice(player1_name)
    choice2 = get_player_choice(player2_name)
    print(f"\n{player1_name} chose {choice1}.")
    print(f"{player2_name} chose {choice2}.")
    result = determine_winner(choice1, choice2)
    print(f"Result: {result}\n")

def rock_paper_scissors_game():
    print("Welcome to the Rock-Paper-Scissors game!")
    
    player1 = "Player 1"
    player2 = "Player 2"

    while True:
        play_round(player1, player2)
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing Rock-Paper-Scissors!")
            break

if __name__ == "__main__":
    rock_paper_scissors_game()
