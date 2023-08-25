file_path = './input_day_02.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

# Initialize a list to store the strategy guide
strategy_guide = []

# Parse the input lines to extract the opponent's choice and your choice
for line in lines_day_2:
    line = line.strip()
    opponent_choice, your_choice = line.split()
    strategy_guide.append((opponent_choice, your_choice))

# Initialize the total score
total_score = 0

# Define a mapping for the score of each shape
shape_score = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

# Iterate through the strategy guide to calculate the score for each round
for opponent_choice, your_choice in strategy_guide:
    # Initialize the score for the current round
    round_score = 0
    
    # Add the score for the shape you selected
    round_score += shape_score[your_choice]
    
    # Determine the outcome of the round and add the corresponding score
    if opponent_choice == 'A':  # Opponent chose Rock
        if your_choice == 'Y':  # You chose Paper, you win
            round_score += 6
        elif your_choice == 'X':  # You also chose Rock, it's a draw
            round_score += 3
    elif opponent_choice == 'B':  # Opponent chose Paper
        if your_choice == 'Z':  # You chose Scissors, you win
            round_score += 6
        elif your_choice == 'Y':  # You also chose Paper, it's a draw
            round_score += 3
    elif opponent_choice == 'C':  # Opponent chose Scissors
        if your_choice == 'X':  # You chose Rock, you win
            round_score += 6
        elif your_choice == 'Z':  # You also chose Scissors, it's a draw
            round_score += 3
    
    # Add the round score to the total score
    total_score += round_score

total_score


#--- Part Two ---

# Initialize the total score again for the new scenario
total_score_new = 0

# Iterate through the strategy guide to calculate the score for each round based on the new interpretation
for opponent_choice, desired_outcome in strategy_guide:
    # Initialize the score for the current round
    round_score = 0
    
    # Determine what shape to choose and the outcome of the round based on the desired outcome
    if desired_outcome == 'X':  # You need to lose
        if opponent_choice == 'A':  # Opponent chose Rock, you choose Scissors to lose
            your_choice = 'Z'
        elif opponent_choice == 'B':  # Opponent chose Paper, you choose Rock to lose
            your_choice = 'X'
        elif opponent_choice == 'C':  # Opponent chose Scissors, you choose Paper to lose
            your_choice = 'Y'
        # You lose, so outcome score is 0
        outcome_score = 0
    elif desired_outcome == 'Y':  # You need to draw
        # To draw, you should choose the same shape as your opponent
        your_choice = opponent_choice
        # It's a draw, so outcome score is 3
        outcome_score = 3
    elif desired_outcome == 'Z':  # You need to win
        if opponent_choice == 'A':  # Opponent chose Rock, you choose Paper to win
            your_choice = 'Y'
        elif opponent_choice == 'B':  # Opponent chose Paper, you choose Scissors to win
            your_choice = 'Z'
        elif opponent_choice == 'C':  # Opponent chose Scissors, you choose Rock to win
            your_choice = 'X'
        # You win, so outcome score is 6
        outcome_score = 6
    
    # Add the score for the shape you selected and the outcome
    round_score += shape_score[your_choice] + outcome_score
    
    # Add the round score to the total score
    total_score_new += round_score

total_score_new
