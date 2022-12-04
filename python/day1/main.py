
def main():
    max_sum = 0
    curr_sum = 0
    sums = []

    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            if line:
                curr_sum += int(line)
            else:
                max_sum = max(max_sum, curr_sum)
                sums.append(curr_sum)
                curr_sum = 0

    sums.sort(reverse=True)

    print(f'Max:   {sums[0]}')
    print(f'Top 3: {sum(sums[:3])}')


if __name__ == '__main__':
    main()
