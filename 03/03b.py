#!/usr/bin/env python

import util


def priority(char: str):
    if char.islower():
        return ord(char) - 96
    if char.isupper():
        return ord(char) - 38


def main():
    priority_sum = 0

    with open(util.input_file) as f:
        def iter_triples():
            while True:
                first = f.readline()
                if not first:
                    return
                first = first.strip()
                second = f.readline().strip()
                third = f.readline().strip()

                yield first, second, third

        for first, second, third in iter_triples():
            first_set = set(c for c in first)
            second_set = set(c for c in second)
            third_set = set(c for c in third)

            common_chars = first_set & second_set & third_set

            for cc in common_chars:
                priority_sum += priority(cc)

    print(f'{priority_sum=}')


if __name__ == '__main__':
    main()
