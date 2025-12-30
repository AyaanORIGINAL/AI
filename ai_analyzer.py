import random
from collections import Counter

def play_round(player_choice, history):
    if history:
        most_common = Counter(history).most_common(1)[0][0]
        counters = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
        ai_move = counters[most_common]
    else:
        ai_move = random.choice(['rock', 'paper', 'scissors'])
    
    history.append(player_choice)
    
    if player_choice == ai_move:
        return "It's a tie!", ai_move
    
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[player_choice] == ai_move:
        return "You win! AI chose", ai_move
    else:
        return "AI wins! AI chose", ai_move

if __name__ == "__main__":
    history = []
    while True:
        player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        if player_choice == 'quit':
            break
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue
        result, ai_move = play_round(player_choice, history)
        print(result, ai_move)
