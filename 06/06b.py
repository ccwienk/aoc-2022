#!/usr/bin/env python

import util


def main():
    with open(util.input_file) as f:
        chars = f.read().strip()

    marker_leng = 14
    for idx in range(len(chars) - marker_leng):
        current = chars[idx: idx + marker_leng]
        if len(set(current)) < marker_leng:
            continue
        break # reached start-of-package-marker

    print(idx + marker_leng)


if __name__ == '__main__':
    main()
