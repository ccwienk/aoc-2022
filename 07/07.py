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


    size_sum = 0
    for d in iter_dirs(tree):
        size = treesize(d)
        if size < 100001:
            size_sum += size

    print(size_sum)

if __name__ == '__main__':
    main()
