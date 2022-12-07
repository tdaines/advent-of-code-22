def main():
    priority_sum = 0
    lines = []

    with open('input.txt') as f:
        for line in f:
            lines.append(line[:-1])

            if len(lines) == 3:
                first = set(lines[0])
                second = set(lines[1])
                third = set(lines[2])

                common = (first & second & third).pop()
                common = ord(common)

                if ord('a') <= common <= ord('z'):
                    priority = common - ord('a') + 1
                else:
                    priority = common - ord('A') + 27

                priority_sum += priority
                lines.clear()

    print(f'Total priority: {priority_sum}')


if __name__ == '__main__':
    main()
