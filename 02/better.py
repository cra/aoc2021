def get_dirs(test=False):
    test = """
    forward 5
    down 5
    forward 8
    up 3
    down 8
    forward 2
    """

    lines = test.strip().splitlines()
    lines = open("puzzle_input").readlines()

    dirs = []
    for line in lines:
        d, v = line.split()
        dirs.append((d, int(v)))

    return dirs

def part1(dirs):
    pos = [0, 0]
    for d, v in dirs:
        if d == "forward":
            pos[0] += v
        elif d == "down":
            pos[1] += v
        elif d == "up":
            pos[1] -= v
    return pos


def part2(dirs):
    pos = [0, 0]
    aim = 0
    for d, v in dirs:
        if d == "forward":
            pos[0] += v
            pos[1] += aim * v
        if d == "down":
            aim += v
        if d == "up":
            aim -= v
    return pos


if __name__ == '__main__':
    dirs = get_dirs(test=False)

    p1 = part1(dirs)
    print("part1", p1, p1[0] * p1[1])

    # -- part 2
    p2 = part2(dirs)
    print("part2", p2, p2[0] * p2[1])
