def get_secret_number(player_name):
    while True:
        secret_number = input(f"{player_name}, please set a multi-digit secret number: ")
        if secret_number.isdigit() and len(secret_number) > 0:
            return secret_number
        print("Invalid input. Please enter a multi-digit number.")

def get_guess(player_name, length):
    while True:
        guess = input(f"{player_name}, make your guess ({length} digits): ")
        if guess.isdigit() and len(guess) == length:
            return guess
        print(f"Invalid input. Please enter a {length}-digit number.")

def give_hint(secret, guess):
    correct_position = sum(1 for s, g in zip(secret, guess) if s == g)
    correct_digits = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
    return correct_position, correct_digits - correct_position

def play_round(setter_name, guesser_name):
    secret_number = get_secret_number(setter_name)
    attempts = 0

    while True:
        attempts += 1
        guess = get_guess(guesser_name, len(secret_number))
        if guess == secret_number:
            print(f"{guesser_name} guessed the number correctly in {attempts} attempts!")
            return attempts
        correct_position, correct_digits = give_hint(secret_number, guess)
        print(f"Hint: {correct_position} digits in the correct position, rest digits in the wrong position.")

def mastermind_game():
    print("Welcome to the Mastermind game!")
    
    # Player names
    player1 = "Player 1"
    player2 = "Player 2"

    # Player 1 sets the number, Player 2 guesses
    print(f"\n{player1}'s turn to set the number.")
    player1_attempts = play_round(player1, player2)

    # Player 2 sets the number, Player 1 guesses
    print(f"\n{player2}'s turn to set the number.")
    player2_attempts = play_round(player2, player1)

    # Determine the winner
    if player1_attempts < player2_attempts:
        print(f"\n{player1} wins and is crowned Mastermind!")
    else:
        print(f"\n{player2} wins and is crowned Mastermind!")

if __name__ == "__main__":
    mastermind_game()
