from functools import partial
from collections import defaultdict
import itertools

test = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


def decipher_entry(entry: str, p2_mode:bool=False):
    lhs, rhs = entry.split(" -> ")
    x1, y1 = tuple(map(int, lhs.split(',')))
    x2, y2 = tuple(map(int, rhs.split(',')))
    points_covered = []
    if x1 == x2:
        y1, y2 = sorted([y1, y2])
        points_covered = [(x1, yi) for yi in range(y1, y2+1)]
    elif y1 == y2:
        x1, x2 = sorted([x1, x2])
        points_covered = [(xi, y1) for xi in range(x1, x2+1)]
    else:
        if p2_mode:
            dx = 1 if x2 > x1 else -1
            dy = 1 if y2 > y1 else -1
            xx, yy = x1, y1
            while xx != x2 and yy != y2:
                points_covered.append((xx, yy))
                xx += dx
                yy += dy
            points_covered.append((x2, y2))


    #print(entry, x1, y1, x2, y2, points_covered)

    return points_covered


def puzzle(lines, decipher, print_board=False):
    max_x, max_y = 0, 0
    board = defaultdict(lambda: 0)
    for line in lines:
        points = decipher(line)
        for x, y in points:
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
            board[x, y] += 1

        print("BOARD after line", line)
        if print_board:
            for yy in range(0, max_y+1):
                for xx in range(0, max_x+1):
                    print(board.get((xx, yy), '.'), end='')
                print()

    num_twoplus = sum(v > 1 for v in board.values())
    return num_twoplus


if __name__ == '__main__':
    decipher_p1 = partial(decipher_entry, p2_mode=False)
    print("p1 test:", puzzle(test.strip().splitlines(), decipher_p1, print_board=True))
    print("p1 puzzle:", puzzle([line.strip() for line in open("./puzzle_input").readlines()], decipher=decipher_p1))

    decipher_p2 = partial(decipher_entry, p2_mode=True)
    #print(decipher_p2("9,7 -> 7,9"))
    #print(decipher_p2("1,1 -> 3,3"))
    print("p2 test:", puzzle(test.strip().splitlines(), decipher_p2, print_board=True))
    print("p2 puzzle:", puzzle([line.strip() for line in open("./puzzle_input").readlines()], decipher=decipher_p2))
