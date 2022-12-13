from collections import deque
from typing import List, Deque


NUM_STACKS = 9


def parse_stacks(line: str, stacks: List[deque]):
    # '[C]         [S] [H]' --> 'C__SH____'
    line = line.strip()
    line = line.replace('  ', ' ')
    line = line.replace('[', '')
    line = line.replace(']', '')
    line = line.replace('  ', ' _')
    line = line.replace(' ', '')
    if len(line) < NUM_STACKS:
        line += '_' * (NUM_STACKS - len(line))

    for i in range(len(line)):
        c = line[i]
        if c != '_':
            stacks[i].appendleft(line[i])


def parse_move_single_crate(line: str, stacks: List[deque]):
    # 'move 15 from 8 to 9'
    move, positions = line.split('from')
    num_moves = int(move[len('move'):])
    source, target = positions.split('to')

    # to zero based index
    source = int(source) - 1
    target = int(target) - 1

    for _ in range(num_moves):
        stacks[target].append(stacks[source].pop())


def parse_move_multiple_crates(line: str, stacks: List[deque]):
    # 'move 15 from 8 to 9'
    move, positions = line.split('from')
    num_moves = int(move[len('move'):])
    source, target = positions.split('to')

    # to zero based index
    source = int(source) - 1
    target = int(target) - 1

    temp = deque()

    for _ in range(num_moves):
        temp.append(stacks[source].pop())

    for _ in range(num_moves):
        stacks[target].append(temp.pop())


def part1():
    stacks = [deque() for i in range(NUM_STACKS)]

    with open('input.txt') as f:
        line_number = 1
        for line in f:
            if line_number < 9:
                parse_stacks(line, stacks)
            elif line_number > 10:
                parse_move_single_crate(line, stacks)
            line_number += 1

    top_crates = ''
    for stack in stacks:
        top_crates += stack.pop()

    print(f'Top crates: {top_crates}')


def part2():
    stacks = [deque() for i in range(NUM_STACKS)]

    with open('input.txt') as f:
        line_number = 1
        for line in f:
            if line_number < 9:
                parse_stacks(line, stacks)
            elif line_number > 10:
                parse_move_multiple_crates(line, stacks)
            line_number += 1

    top_crates = ''
    for stack in stacks:
        top_crates += stack.pop()

    print(f'Top crates: {top_crates}')


if __name__ == '__main__':
    part1()
    part2()
