#!/usr/bin/env python

import util


def visible_for_seq(seq: list[int]):
    def iter_row(seq):
        tallest = seq[0]
        yield 0

        for idx, t in enumerate(seq[1:], 1):
            if t <= tallest:
                continue # previous trees were taller (or equally tall)
            tallest = t
            yield idx

    visible_tree_idxs = set(iter_row(seq))

    for idx in iter_row(list(reversed(seq))):
        reversed_idx = (len(seq) - 1) - idx
        visible_tree_idxs.add(reversed_idx)

    return visible_tree_idxs


def main():
    with open(util.input_file) as f:
        grid = [
            [
                int(col) for col in
                row.strip()
            ]
            for row in f.readlines()
        ]

    # grid[row-idx][col-idx]

    rows = len(grid)
    cols = len(grid[0])

    visible_trees = dict()
    for row in range(0, rows):
        for col in range(0, cols):
            if row == 0 or row == (rows - 1) or col == 0 or col == (cols - 1):
                visible = True
            else:
                visible = False

            visible_trees[(row, col)] = visible

    # iter rows
    for row_idx, row in enumerate(grid):
        for col_idx in visible_for_seq(row):
            visible_trees[(row_idx, col_idx)] = True

    def iter_col(col_idx):
        for row_idx in range(rows):
            yield grid[row_idx][col_idx]

    for col_idx in range(cols):
        column = list(iter_col(col_idx))
        visible_tree_idxs =  visible_for_seq(column)
        for row_idx in visible_tree_idxs:
            visible_trees[(row_idx, col_idx)] = True

    visible_count = len([visible for visible in visible_trees.values() if visible])

    print(visible_count)


if __name__ == '__main__':
    main()
