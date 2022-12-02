#!/usr/bin/env python

import util

rock = 'A', 'X'
paper = 'B', 'Y'
scissors = 'C', 'Z'


def calculate_score(opponent, reply):
    if reply in rock:
        score = 1
    elif reply in paper:
        score = 2
    elif reply in scissors:
        score = 3
    else:
        raise ValueError(reply)

    if opponent in rock:
        if reply in scissors:
            return score + 0 # we lost
        elif reply in paper:
            return score + 6
        elif reply in rock:
            return score + 3 # draw
        else:
            raise ValueError(opponent)
    elif opponent in paper:
        if reply in rock:
            return score + 0 # we lost
        elif reply in scissors:
            return score + 6
        elif reply in paper:
            return score + 3 # draw
        else:
            raise ValueError(opponent)
    elif opponent in scissors:
        if reply in paper:
            return score + 0 # we lost
        elif reply in rock:
            return score + 6
        elif reply in scissors:
            return score + 3 # draw
        else:
            raise ValueError(opponent)
    else:
        raise ValueError(opponent)


def main():
    score = 0
    with open(util.input_file) as f:
        for line in f.readlines():
            line = line.strip()
            opponent, reply = line.split(' ')
            score += calculate_score(opponent, reply)

    print(score)


if __name__ == '__main__':
    main()
