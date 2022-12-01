#!/usr/bin/env python

import util


def main():
    sums = []

    current_sum = 0

    with open(util.input_file) as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                current_sum += int(line)
            else: # reached end of block
                sums.append(current_sum)
                current_sum = 0

    sums = sorted(sums, reverse=True) # greatest value first

    top_three = sums[0:3]

    print(f'max: {top_three[0]}')
    print(f'sum of top-three: {sum(top_three)}')


if __name__ == '__main__':
    main()
