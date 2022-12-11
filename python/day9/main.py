from enum import Enum


class Direction(Enum):
    UP = 'U'
    UP_RIGHT = 'UR'
    RIGHT = 'R'
    DOWN_RIGHT = 'DR'
    DOWN = 'D'
    DOWN_LEFT = 'DL'
    LEFT = 'L'
    UP_LEFT = 'UL'


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return repr((self.x, self.y))

    def __eq__(self, other: 'Point'):
        return self.x == other.x and self.y == other.y

    def move(self, direction: Direction):
        if Direction.UP.value in direction.value:
            self.y += 1
        elif Direction.DOWN.value in direction.value:
            self.y -= 1

        if Direction.RIGHT.value in direction.value:
            self.x += 1
        elif Direction.LEFT.value in direction.value:
            self.x -= 1

    def touching(self, other: 'Point') -> bool:
        x_diff = abs(self.x - other.x)
        y_diff = abs(self.y - other.y)

        return x_diff <= 1 and y_diff <= 1

    def move_to(self, other: 'Point'):
        # Same row
        if self.y == other.y:
            self.move(Direction.RIGHT if other.x > self.x else Direction.LEFT)
        # Same col
        elif self.x == other.x:
            self.move(Direction.UP if other.y > self.y else Direction.DOWN)
        # Diagonal up
        elif other.y > self.y:
            self.move(Direction.UP_RIGHT if other.x > self.x else Direction.UP_LEFT)
        else:  # Diagonal down
            self.move(Direction.DOWN_RIGHT if other.x > self.x else Direction.DOWN_LEFT)


def main():
    head = Point(0, 0)
    tail = Point(0, 0)
    visited = set()

    visited.add((tail.x, tail.y))

    print(f'S: H - ({head.x}, {head.y}), T - ({tail.x}, {tail.y})')

    with open('input.txt') as f:
        for line in f:
            direction = Direction(line[0])
            steps = int(line[2])
            for _ in range(steps):
                head.move(direction)
                if not tail.touching(head):
                    tail.move_to(head)
                    visited.add((tail.x, tail.y))
                print(f'{direction.value}: H - ({head.x}, {head.y}), T - ({tail.x}, {tail.y})')

    print(f'Tail visited {len(visited)} positions')


if __name__ == '__main__':
    main()


def test_touching():
    assert Point(0, 0).touching(Point(0, 0))    # OVERLAP
    assert Point(0, 0).touching(Point(0, 1))    # UP
    assert Point(0, 0).touching(Point(1, 1))    # UP RIGHT
    assert Point(0, 0).touching(Point(1, 0))    # RIGHT
    assert Point(0, 0).touching(Point(1, -1))   # DOWN RIGHT
    assert Point(0, 0).touching(Point(0, -1))   # DOWN
    assert Point(0, 0).touching(Point(-1, -1))  # DOWN LEFT
    assert Point(0, 0).touching(Point(-1, 0))   # LEFT
    assert Point(0, 0).touching(Point(-1, 1))   # UP LEFT


def test_not_touching():
    assert not Point(0, 0).touching(Point(0, 2))    # UP
    assert not Point(0, 0).touching(Point(2, 1))    # UP RIGHT
    assert not Point(0, 0).touching(Point(1, 2))    # UP RIGHT
    assert not Point(0, 0).touching(Point(2, 0))    # RIGHT
    assert not Point(0, 0).touching(Point(2, -1))   # DOWN RIGHT
    assert not Point(0, 0).touching(Point(1, -2))   # DOWN RIGHT
    assert not Point(0, 0).touching(Point(0, -2))   # DOWN
    assert not Point(0, 0).touching(Point(-2, -1))  # DOWN LEFT
    assert not Point(0, 0).touching(Point(-1, -2))  # DOWN LEFT
    assert not Point(0, 0).touching(Point(-2, 0))   # LEFT
    assert not Point(0, 0).touching(Point(-2, 1))   # UP LEFT
    assert not Point(0, 0).touching(Point(-1, 2))   # UP LEFT


def test_move_to():
    # UP
    p = Point(0, 0)
    p.move_to(Point(0, 2))
    assert p == Point(0, 1)

    # UP RIGHT
    p = Point(0, 0)
    p.move_to(Point(2, 1))
    assert p == Point(1, 1)

    p = Point(0, 0)
    p.move_to(Point(1, 2))
    assert p == Point(1, 1)

    # RIGHT
    p = Point(0, 0)
    p.move_to(Point(2, 0))
    assert p == Point(1, 0)

    # DOWN RIGHT
    p = Point(0, 0)
    p.move_to(Point(2, -1))
    assert p == Point(1, -1)

    p = Point(0, 0)
    p.move_to(Point(1, -2))
    assert p == Point(1, -1)

    # DOWN
    p = Point(0, 0)
    p.move_to(Point(0, -2))
    assert p == Point(0, -1)

    # DOWN LEFT
    p = Point(0, 0)
    p.move_to(Point(-2, -1))
    assert p == Point(-1, -1)

    p = Point(0, 0)
    p.move_to(Point(-1, -2))
    assert p == Point(-1, -1)

    # LEFT
    p = Point(0, 0)
    p.move_to(Point(-2, 0))
    assert p == Point(-1, 0)

    # UP LEFT
    p = Point(0, 0)
    p.move_to(Point(-2, 1))
    assert p == Point(-1, 1)

    p = Point(0, 0)
    p.move_to(Point(-1, 2))
    assert p == Point(-1, 1)
