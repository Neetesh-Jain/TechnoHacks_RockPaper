import random

def play_round(player_type):
    # Define possible choices
    choices = {'rock': 'Rock', 'paper': 'Paper', 'scissors': 'Scissors'}
    
    if player_type == "computer":
        # Get player's input
        player_choice = input("\nChoose (rock, paper, or scissors): ").lower()
        
        # Validate input
        if player_choice not in choices:
            print("Invalid choice! Please select rock, paper, or scissors.")
            return None, None
        
        # Computer's choice
        computer_choice = random.choice(list(choices.keys()))

        print(f"\nYou chose: {choices[player_choice]}")
        print(f"Computer chose: {choices[computer_choice]}")

    else:  # Two-player mode
        player_choice = input("\nPlayer 1, choose (rock, paper, or scissors): ").lower()
        if player_choice not in choices:
            print("Invalid choice! Please select rock, paper, or scissors.")
            return None, None
        print(f"Player 1 chose: {choices[player_choice]}")
        
        player_choice_2 = input("Player 2, choose (rock, paper, or scissors): ").lower()
        if player_choice_2 not in choices:
            print("Invalid choice! Please select rock, paper, or scissors.")
            return None, None
        print(f"Player 2 chose: {choices[player_choice_2]}")
        
        computer_choice = None  # No computer choice in two-player mode

    # Determine the winner of the round
    if player_type == "computer":
        if player_choice == computer_choice:
            print("It's a tie!")
            return 0, 0  # No points for tie
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'scissors' and computer_choice == 'paper') or \
             (player_choice == 'paper' and computer_choice == 'rock'):
            print("You win this round!")
            return 1, 0  # Player gets 1 point
        else:
            print("Computer wins this round!")
            return 0, 1  # Computer gets 1 point
    else:  # Two-player mode
        if player_choice == player_choice_2:
            print("It's a tie!")
            return 0, 0  # No points for tie
        elif (player_choice == 'rock' and player_choice_2 == 'scissors') or \
             (player_choice == 'scissors' and player_choice_2 == 'paper') or \
             (player_choice == 'paper' and player_choice_2 == 'rock'):
            print("Player 1 wins this round!")
            return 1, 0  # Player 1 gets 1 point
        else:
            print("Player 2 wins this round!")
            return 0, 1  # Player 2 gets 1 point

def play_game():
    print("Welcome to Rock, Paper, Scissors!\n")
    
    # Choose mode: against computer or another player
    mode = input("Do you want to play against a computer or another player? (computer/player): ").lower()
    if mode not in ['computer', 'player']:
        print("Invalid mode selected. Please choose 'computer' or 'player'.")
        return
    
    rounds = int(input("How many rounds do you want to play? "))
    
    # Initialize scores
    player1_score = 0
    player2_score = 0

    # Play multiple rounds
    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        if mode == 'computer':
            player_points, computer_points = play_round("computer")
            if player_points is not None:
                player1_score += player_points
                player2_score += computer_points
        else:
            player_points, computer_points = play_round("player")
            if player_points is not None:
                player1_score += player_points
                player2_score += computer_points

    # Final score
    print("\n--- Game Over ---")
    print(f"Final Score: Player 1 {player1_score} - {player2_score} Player 2")
    
    if player1_score > player2_score:
        print("Congratulations, Player 1 won the game!")
    elif player1_score < player2_score:
        print("Oh no, Player 2 won the game!")
    else:
        print("It's a tie game!")

    # Ask if the player wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()  # Recursion to start a new game
    else:
        print("Thanks for playing! Goodbye!")

# Start the game
play_game()
