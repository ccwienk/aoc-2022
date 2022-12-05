#!/usr/bin/env python

import util


def iter_crates(line: str):
    line = line.removesuffix('\n')

    for offset in range(1, 9 * 4, 4):
        if offset >= len(line):
            yield None
            continue

        crate = line[offset]
        if crate == ' ':
            yield None
        else:
            yield crate


def main():
    cratestacks = [[] for _ in range(9)] # idx 0: bottom

    processing_crates = True

    with open(util.input_file) as f:
        for line in f.readlines():
            if processing_crates:
                if not line.startswith('['):
                    processing_crates = False
                    # skip numbers + empty line
                    f.readline()
                else:
                    for idx, c in enumerate(iter_crates(line)):
                        if c:
                            cratestacks[idx].insert(0, c)
                continue

            line = line.strip()
            if not line:
                continue

            _, count, _, src, _, tgt = line.split(' ')
            count = int(count)
            src = cratestacks[int(src) - 1]
            tgt = cratestacks[int(tgt) - 1]

            crates_to_mv = []
            for _ in range(count):
                crates_to_mv.insert(0, src.pop())

            tgt.extend(crates_to_mv)

        for c in cratestacks:
            print(c[-1], end='')
        print()

if __name__ == '__main__':
    main()
