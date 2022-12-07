def main():
    priority_sum = 0

    with open('input.txt') as f:
        for line in f:
            mid = int(len(line) / 2)
            first_half = set(line[:mid])
            second_half = set(line[mid:])

            common = first_half.intersection(second_half).pop()
            common = ord(common)
            if ord('a') <= common <= ord('z'):
                priority = common - ord('a') + 1
            else:
                priority = common - ord('A') + 27

            priority_sum += priority

    print(f'Total priority: {priority_sum}')


if __name__ == '__main__':
    main()
