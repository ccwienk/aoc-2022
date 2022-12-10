#!/usr/bin/env python

import util


def main():
    cycle = 1
    x = 1
    sig_strength = 0

    instructions = {} # target-cycle: xdiff

    pixels = [
        [' ' for _ in range(40)],
        [' ' for _ in range(40)],
        [' ' for _ in range(40)],
        [' ' for _ in range(40)],
        [' ' for _ in range(40)],
        [' ' for _ in range(40)],
    ]

    def end_cycle():
        nonlocal cycle
        nonlocal instructions
        nonlocal x
        nonlocal sig_strength

        # print(f'beginning {cycle=} {x=}')
        if cycle == 20 or cycle >= 60 and ((cycle - 20) % 40 == 0):
            #print(f'{cycle=} {cycle * x=}')
            sig_strength += cycle * x

        rowpos = (cycle - 1) % 40
        if rowpos == x or rowpos - 1 == x or rowpos + 1 == x:
            # print pixel
            row = int((cycle -1) / 40)
            pixels[row][rowpos] = 'x'

        if cycle in instructions:
            x += instructions.pop(cycle)


        cycle += 1

    with open(util.input_file) as f:
        for line in f.readlines():
            line = line.strip()

            if line == 'noop':
                end_cycle()
                continue

            # all other instructions are `addx`, so don't bother splitting
            arg = int(line.removeprefix('addx '))

            instructions[cycle + 1] = arg
            end_cycle()
            end_cycle()

    end_cycle()
    end_cycle()

    for row in pixels:
        for p in row:
            print(p, end='')
        print()

    print(sig_strength)


if __name__ == '__main__':
    main()
