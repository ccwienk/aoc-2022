#!/usr/bin/env python

import util


def posdiff(left, right):
    x0, y0 = left
    x1, y1 = right

    return x0 - x1, y0 - y1


def adjacent(left, right):
    def iter_adjacent(pos):
        x, y = pos

        yield x - 1, y
        yield x - 1, y - 1
        yield x - 1, y + 1

        yield x + 1, y
        yield x + 1, y - 1
        yield x + 1, y + 1

        yield x, y - 1
        yield x, y + 1
        yield x,y

    if left == right:
        return True

    for p in iter_adjacent(pos=left):
        if p == right:
            return True
    else:
        return False


def main():
    visited = {(0,0)}

    h_pos = 0, 0
    t_pos = 0, 0


    def update_hpos(xdiff=0, ydiff=0):
        nonlocal h_pos
        h_pos = h_pos[0] + xdiff, h_pos[1] + ydiff


    def update_tpos(direction):
        nonlocal h_pos
        nonlocal t_pos
        nonlocal visited

        # check if adjacent
        hx, hy = h_pos
        tx, ty = t_pos

        if adjacent(h_pos, t_pos):
            return # adjacent, nothing to do

        xdiff, ydiff = posdiff(h_pos, t_pos)

        if xdiff == 0:
            if ydiff == 2:
                t_pos = tx, ty + 1
            elif ydiff == -2:
                t_pos = tx, ty - 1
            else:
                raise ValueError(ydiff)
        elif ydiff == 0:
            if xdiff == 2:
                t_pos = tx + 1, ty
            elif xdiff == -2:
                t_pos = tx - 1, ty
            else:
                raise ValueError(xdiff)
        elif abs(xdiff) == 2 and ydiff == 1:
            t_pos = hx, ty + 1
        elif abs(xdiff) == 2 and ydiff == -1:
            t_pos = hx, ty - 1
        elif xdiff == -1 and abs(ydiff) == 2:
            t_pos = tx - 1, hy
        elif xdiff == 1 and abs(ydiff) == 2:
            t_pos = tx + 1, hy
        else:
            print(h_pos)
            print(t_pos)
            raise ValueError((xdiff, ydiff))

        if not adjacent(h_pos, t_pos):
            raise RuntimeError()

        visited.add(t_pos)


    with open(util.input_file) as f:
        for line in f.readlines():
            direction, count = line.strip().split(' ')
            count = int(count)

            if direction == 'U': # up
                xdiff = 0
                ydiff = 1
            elif direction == 'D': # down
                xdiff = 0
                ydiff = -1
            elif direction == 'L': # left
                xdiff = -1
                ydiff = 0
            elif direction == 'R': # right
                xdiff = 1
                ydiff = 0

            print(f'{direction} {count}')
            print(f'{h_pos} {t_pos}')
            for _ in range(count):
                update_hpos(xdiff, ydiff)
                update_tpos(direction)
            print(f'{h_pos} {t_pos}')
            print('----')

    print(len(visited))
    # 4773: too low
    # 5728: too low


if __name__ == '__main__':
    main()
