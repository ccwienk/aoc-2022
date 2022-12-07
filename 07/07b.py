#!/usr/bin/env python

import util


def treesize(tree: dict):
    size = 0
    for k,v in tree.items():
        if isinstance(v, int):
            size += v
        elif isinstance(v, dict):
            size += treesize(tree=v)
    return size


def iter_dirs(tree: dict):
    for k,v in tree.items():
        if isinstance(v, dict):
            yield v
            yield from iter_dirs(v)


def main():
    tree = {'/': {}} # pre-initialise root-directory to avoid special-case
    total_fsize = 0

    with open(util.input_file) as f:
        path = []
        while line := f.readline():
            line = line.strip()
            is_cmd = line[0] == '$'
            if is_cmd:
                line = line.removeprefix('$ ')
                cmd = line[:2]
                if len(line) > 2:
                    arg = line[3:]
                else:
                    arg = ''

                if cmd == 'cd':
                    if arg == '..':
                        path.pop()
                    else:
                        path.append(arg)
                elif cmd == 'ls':
                    continue
                else:
                    raise ValueError(cmd)
            else:
                left, name = line.split(' ')

                # select parent-dir
                pdir = tree[path[0]]
                for p in path[1:]:
                    pdir = pdir[p]

                if left == 'dir':
                    pdir[name] = {} # found new directory
                else:
                    size = int(left)
                    pdir[name] = size # found new file
                    total_fsize += size


    total_size =    70000000
    required_free = 30000000

    dirsizes = []

    for d in iter_dirs(tree):
        size = treesize(d)
        dirsizes.append(size)

    current_free = total_size - total_fsize
    need_to_rm = required_free - current_free

    print(f'{total_fsize=}')
    print(f'{current_free=}')
    print(f'{need_to_rm=}')

    dirsizes = [d for d in dirsizes if d >= need_to_rm]

    best_dirsize = dirsizes[0]
    best_overshoot = best_dirsize - need_to_rm

    for dirsize in dirsizes:
        overshoot = dirsize - need_to_rm
        if overshoot < best_overshoot:
            best_overshoot = overshoot
            best_dirsize = dirsize

    print(f'{best_dirsize=}')


if __name__ == '__main__':
    main()
