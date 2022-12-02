#!/usr/bin/env python

import util

rock = 'A'
paper = 'B'
scissors = 'C'

lose = 'X'
draw = 'Y'
win = 'Z'


def calculate_score(opponent, reply):
    if reply == rock:
        score = 1
    elif reply == paper:
        score = 2
    elif reply == scissors:
        score = 3
    else:
        raise ValueError(reply)

    if opponent == rock:
        if reply == scissors:
            return score + 0 # we lost
        elif reply == paper:
            return score + 6
        elif reply == rock:
            return score + 3 # draw
        else:
            raise ValueError(opponent)
    elif opponent == paper:
        if reply == rock:
            return score + 0 # we lost
        elif reply == scissors:
            return score + 6
        elif reply == paper:
            return score + 3 # draw
        else:
            raise ValueError(opponent)
    elif opponent == scissors:
        if reply == paper:
            return score + 0 # we lost
        elif reply == rock:
            return score + 6
        elif reply == scissors:
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
            if reply == draw:
                own = opponent
            elif reply == win:
                if opponent == rock:
                    own = paper
                elif opponent == paper:
                    own = scissors
                elif opponent == scissors:
                    own = rock
            elif reply == lose:
                if opponent == rock:
                    own = scissors
                elif opponent == paper:
                    own = rock
                elif opponent == scissors:
                    own = paper

            score += calculate_score(opponent, own)

    print(score)


if __name__ == '__main__':
    main()
