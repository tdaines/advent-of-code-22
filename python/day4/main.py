def part1():
    count = 0
    with open('input.txt') as f:
        for line in f:
            # '22-44,33-55'
            first, second = line.split(',')

            start, end = first.split('-')
            left = set(range(int(start), int(end) + 1))

            start, end = second.split('-')
            right = set(range(int(start), int(end) + 1))

            if left.issubset(right) or right.issubset(left):
                count += 1

    print(f'In {count} assignment pairs does one range fully contain the other')


def part2():
    count = 0
    with open('input.txt') as f:
        for line in f:
            first, second = line.split(',')

            start, end = first.split('-')
            left = set(range(int(start), int(end) + 1))

            start, end = second.split('-')
            right = set(range(int(start), int(end) + 1))

            if left.intersection(right):
                count += 1

    print(f'In {count} assignment pairs does one range fully contain the other')


if __name__ == '__main__':
    part1()
    part2()
