



# Points
# 1 - Rock
# 2 - Paper
# 3 - Scissors

# 0 - Loss
# 3 - Draw
# 6 - Win

from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Result(Enum):
    WIN = 1
    LOSE = 2
    DRAW = 3


def main():
    score = 0
    with open('input.txt') as f:
        for line in f:
            opponent, player = line.split()
            score += play(opponent, player)

    print(f'Final score: {score}')


def play(opponent: str, player: str) -> int:
    player = convert_move(player)
    opponent = convert_move(opponent)

    result = get_result(player, opponent)
    score = get_score(player, result)

    return score


def convert_move(move: str) -> RPS:
    if move == 'A' or move == 'X':
        return RPS.ROCK

    if move == 'B' or move == 'Y':
        return RPS.PAPER

    if move == 'C' or move == 'Z':
        return RPS.SCISSORS

    raise Exception(f'Unknown move {move}')


def get_result(player: RPS, opponent: RPS) -> Result:
    if player == RPS.ROCK:
        if opponent == RPS.ROCK:
            return Result.DRAW
        if opponent == RPS.PAPER:
            return Result.LOSE
        return Result.WIN

    if player == RPS.PAPER:
        if opponent == RPS.ROCK:
            return Result.WIN
        if opponent == RPS.PAPER:
            return Result.DRAW
        return Result.LOSE

    if player == RPS.SCISSORS:
        if opponent == RPS.ROCK:
            return Result.LOSE
        if opponent == RPS.PAPER:
            return Result.WIN
        return Result.DRAW


def get_score(player: RPS, result: Result) -> int:
    score = 0

    if player == RPS.ROCK:
        score += 1
    elif player == RPS.PAPER:
        score += 2
    else:
        score += 3

    if result == Result.WIN:
        score += 6
    elif result == Result.DRAW:
        score += 3

    return score


if __name__ == '__main__':
    main()


def test_convert_player_move():
    assert convert_move('X') == RPS.ROCK
    assert convert_move('Y') == RPS.PAPER
    assert convert_move('Z') == RPS.SCISSORS

    assert convert_move('A') == RPS.ROCK
    assert convert_move('B') == RPS.PAPER
    assert convert_move('C') == RPS.SCISSORS


def test_get_result():
    assert get_result(RPS.ROCK, RPS.ROCK) == Result.DRAW
    assert get_result(RPS.ROCK, RPS.PAPER) == Result.LOSE
    assert get_result(RPS.ROCK, RPS.SCISSORS) == Result.WIN

    assert get_result(RPS.PAPER, RPS.ROCK) == Result.WIN
    assert get_result(RPS.PAPER, RPS.PAPER) == Result.DRAW
    assert get_result(RPS.PAPER, RPS.SCISSORS) == Result.LOSE

    assert get_result(RPS.SCISSORS, RPS.ROCK) == Result.LOSE
    assert get_result(RPS.SCISSORS, RPS.PAPER) == Result.WIN
    assert get_result(RPS.SCISSORS, RPS.SCISSORS) == Result.DRAW


def test_play():
    assert play('A', 'Y') == 8
    assert play('B', 'X') == 1
    assert play('C', 'Z') == 6
