#!/usr/bin/env python

import util


def priority(char: str):
    if char.islower():
        return ord(char) - 96
    if char.isupper():
        return ord(char) - 38


def main():
    prioty_sum = 0

    with open(util.input_file) as f:
        for line in f.readlines():
            line = line.strip()
            left, right = line[0: (l:=int(len(line)/2))], line[l:]

            left_charset = set(c for c in left)
            right_charset = set(c for c in right)

            common_chars = left_charset & right_charset

            for cc in common_chars:
                prioty_sum += priority(cc)

    print(f'{prioty_sum=}')


if __name__ == '__main__':
    main()
