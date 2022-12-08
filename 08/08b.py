#!/usr/bin/env python

import util


def visible_trees_score(seq: list[int], idx: int):
    fwd_seq = seq[idx:]

    def calc_score(seq):
        start = seq[0]
        count = 0

        for t in seq[1:]:
            count += 1
            if t >= start:
                return count
        return count

    score = calc_score(fwd_seq)
    if score == 0:
        return score

    bwd_seq = list(reversed(seq))[(len(seq) -1) - idx:]
    score *= calc_score(bwd_seq)
    return score


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

    visible_tree_scores = dict()

    for row in range(0, rows):
        for col in range(0, cols):
            visible_tree_scores[(row, col)] = 0

    # iter rows
    for row_idx, row in enumerate(grid):
        for col_idx in range(cols):
            score = visible_trees_score(seq=row, idx=col_idx)
            visible_tree_scores[(row_idx, col_idx)] = score

    def iter_col(col_idx):
        for row_idx in range(rows):
            yield grid[row_idx][col_idx]

    for col_idx in range(cols):
        column = list(iter_col(col_idx))
        for row_idx in range(rows):
            score = visible_trees_score(seq=column, idx=row_idx)
            visible_tree_scores[(row_idx, col_idx)] *= score

    max_score = 0

    for score in visible_tree_scores.values():
        max_score = max(max_score, score)

    print(max_score)


if __name__ == '__main__':
    main()
