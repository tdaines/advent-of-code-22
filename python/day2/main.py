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


def play(opponent: str, result: str) -> int:
    opponent = convert_move(opponent)
    desired_result = convert_result(result)

    player = get_move(opponent, desired_result)
    score = get_score(player, desired_result)

    return score


def convert_move(move: str) -> RPS:
    if move == 'A':
        return RPS.ROCK

    if move == 'B':
        return RPS.PAPER

    if move == 'C':
        return RPS.SCISSORS

    raise Exception(f'Unknown move {move}')


def convert_result(result: str) -> Result:
    if result == 'X':
        return Result.LOSE

    if result == 'Y':
        return Result.DRAW

    if result == 'Z':
        return Result.WIN

    raise Exception(f'Unknown result {result}')


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


def get_move(opponent: RPS, desired_result: Result) -> RPS:
    if opponent == RPS.ROCK:
        if desired_result == Result.WIN:
            return RPS.PAPER
        if desired_result == Result.LOSE:
            return RPS.SCISSORS
        return RPS.ROCK

    if opponent == RPS.PAPER:
        if desired_result == Result.WIN:
            return RPS.SCISSORS
        if desired_result == Result.LOSE:
            return RPS.ROCK
        return RPS.PAPER

    if opponent == RPS.SCISSORS:
        if desired_result == Result.WIN:
            return RPS.ROCK
        if desired_result == Result.LOSE:
            return RPS.PAPER
        return RPS.SCISSORS


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
    assert convert_move('A') == RPS.ROCK
    assert convert_move('B') == RPS.PAPER
    assert convert_move('C') == RPS.SCISSORS


def test_convert_result():
    assert convert_result('X') == Result.LOSE
    assert convert_result('Y') == Result.DRAW
    assert convert_result('Z') == Result.WIN

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


def test_get_score():
    assert get_score(RPS.ROCK, Result.WIN) == 7
    assert get_score(RPS.ROCK, Result.LOSE) == 1
    assert get_score(RPS.ROCK, Result.DRAW) == 4

    assert get_score(RPS.PAPER, Result.WIN) == 8
    assert get_score(RPS.PAPER, Result.LOSE) == 2
    assert get_score(RPS.PAPER, Result.DRAW) == 5

    assert get_score(RPS.SCISSORS, Result.WIN) == 9
    assert get_score(RPS.SCISSORS, Result.LOSE) == 3
    assert get_score(RPS.SCISSORS, Result.DRAW) == 6


def test_play():
    assert play('A', 'Y') == 4
    assert play('B', 'X') == 1
    assert play('C', 'Z') == 7


def test_get_move():
    assert get_move(RPS.ROCK, Result.WIN) == RPS.PAPER
    assert get_move(RPS.ROCK, Result.LOSE) == RPS.SCISSORS
    assert get_move(RPS.ROCK, Result.DRAW) == RPS.ROCK

    assert get_move(RPS.PAPER, Result.WIN) == RPS.SCISSORS
    assert get_move(RPS.PAPER, Result.LOSE) == RPS.ROCK
    assert get_move(RPS.PAPER, Result.DRAW) == RPS.PAPER

    assert get_move(RPS.SCISSORS, Result.WIN) == RPS.ROCK
    assert get_move(RPS.SCISSORS, Result.LOSE) == RPS.PAPER
    assert get_move(RPS.SCISSORS, Result.DRAW) == RPS.SCISSORS
