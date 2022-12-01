#!/usr/bin/env python

import util


def main():
    max_sum = 0

    current_sum = 0

    with open(util.input_file) as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                current_sum += int(line)
                max_sum = max(max_sum, current_sum)
            else: # reached end of block
                current_sum = 0

    print(max_sum)


if __name__ == '__main__':
    main()
