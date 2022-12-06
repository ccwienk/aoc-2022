#!/usr/bin/env python

import util


def main():
    with open(util.input_file) as f:
        chars = f.read().strip()

    for idx in range(len(chars) - 4):
        current = chars[idx: idx + 4]
        if len(set(current)) < 4:
            continue
        break # reached start-of-package-marker

    print(idx + 4)


if __name__ == '__main__':
    main()
