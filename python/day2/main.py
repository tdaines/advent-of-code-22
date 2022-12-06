def main():
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    WIN = 0
    LOSE = 1
    DRAW = 2

    move_lookup = [ROCK, PAPER, SCISSORS]
    result_lookup = [LOSE, DRAW, WIN]
    player_move_lookup = [
        [PAPER, SCISSORS, ROCK],  # Rock
        [SCISSORS, ROCK, PAPER],  # Paper
        [ROCK, PAPER, SCISSORS],  # Scissors
    ]
    move_score_lookup = [1, 2, 3]  # Rock, Paper, Scissors
    result_score_lookup = [6, 0, 3]  # Win, Lose, Draw

    A = ord('A')
    X = ord('X')
    score = 0

    with open('input.txt') as f:
        for line in f:
            opponent = move_lookup[ord(line[0]) - A]
            desired_result = result_lookup[ord(line[2]) - X]
            player = player_move_lookup[opponent][desired_result]

            score += move_score_lookup[player]
            score += result_score_lookup[desired_result]

    print(f'Final score: {score}')


if __name__ == '__main__':
    main()
