#!/usr/bin/env python

import util


def rangeset(rangestr):
    left, right = rangestr.split('-')
    left = int(left)
    right = int(right)

    return set(range(left, right + 1))


def main():
    subset_pairs = 0

    with open(util.input_file) as f:
        for line in f.readlines():
            line = line.strip()
            left, right = line.split(',')

            leftset = rangeset(left)
            rightset = rangeset(right)

            if leftset.issubset(rightset) or rightset.issubset(leftset):
                subset_pairs += 1

    print(subset_pairs)


if __name__ == '__main__':
    main()
