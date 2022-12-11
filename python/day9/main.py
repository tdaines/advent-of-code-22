class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return repr((self.x, self.y))

    def __eq__(self, other: 'Point'):
        return self.x == other.x and self.y == other.y

    def __add__(self, other: 'Point'):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point'):
        return Point(self.x - other.x, self.y - other.y)

    def move(self, direction: str):
        if direction == 'U':
            return self + UP

        if direction == 'D':
            return self + DOWN

        if direction == 'L':
            return self + LEFT

        if direction == 'R':
            return self + RIGHT

    def follow(self, other: 'Point'):
        diff = other - self

        # Overlapping
        if diff == Point(0, 0):
            return self

        # Touching up, down, left, or right
        if diff == UP or diff == DOWN or diff == LEFT or diff == RIGHT:
            return self

        # Touching diagonally
        if diff == (UP + RIGHT) or diff == (UP + LEFT) or diff == (DOWN + LEFT) or diff == (DOWN + RIGHT):
            return self

        # Need to move up
        if diff == (UP + UP):
            return self + UP

        # Need to move down
        if diff == (DOWN + DOWN):
            return self + DOWN

        # Need to move right
        if diff == (RIGHT + RIGHT):
            return self + RIGHT

        # Need to move left
        if diff == (LEFT + LEFT):
            return self + LEFT

        if diff == (RIGHT + RIGHT + UP) or \
                diff == (UP + UP + RIGHT) or \
                diff == (UP + UP + RIGHT + RIGHT):
            return self + UP + RIGHT

        if diff == (RIGHT + RIGHT + DOWN) or \
                diff == (DOWN + DOWN + RIGHT) or \
                diff == (DOWN + DOWN + RIGHT + RIGHT):
            return self + DOWN + RIGHT

        if diff == (LEFT + LEFT + UP) or \
                diff == (UP + UP + LEFT) or \
                diff == (UP + UP + LEFT + LEFT):
            return self + UP + LEFT

        if diff == (LEFT + LEFT + DOWN) or \
                diff == (DOWN + DOWN + LEFT) or \
                diff == (DOWN + DOWN + LEFT + LEFT):
            return self + DOWN + LEFT

        raise Exception(f'Unhandled diff: {diff}')


UP = Point(0, 1)
DOWN = Point(0, -1)
LEFT = Point(-1, 0)
RIGHT = Point(1, 0)


def part1():
    head = Point(0, 0)
    tail = Point(0, 0)

    visited = set()
    visited.add((tail.x, tail.y))

    with open('input.txt') as f:
        for line in f:
            direction = line[0]
            steps = int(line[2:])
            for _ in range(steps):
                head = head.move(direction)
                tail = tail.follow(head)
                visited.add((tail.x, tail.y))

    print(f'Tail visited {len(visited)} positions')


def part2():
    knots = [Point(0, 0)] * 10
    tail = knots[-1]

    visited = set()
    visited.add((tail.x, tail.y))

    with open('input.txt') as f:
        for line in f:
            direction = line[0]
            steps = int(line[2:])
            for _ in range(steps):
                # move head
                knots[0] = knots[0].move(direction)

                # move following knots
                for i in range(1, len(knots)):
                    knots[i] = knots[i].follow(knots[i - 1])

                # record tail
                tail = knots[-1]
                visited.add((tail.x, tail.y))

    print(f'Tail visited {len(visited)} position{"s" if len(visited) != 1 else ""}')


if __name__ == '__main__':
    part2()
