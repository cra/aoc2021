def part1(lines):
    seq = list(map(int, lines))
    print(f'total: {len(seq)}')
    num_incr = sum(
        cur > prev for prev, cur in zip(seq[0:-1], seq[1:])
    )

    return num_incr


p1_test = """
199
200
208
210
200
207
240
269
260
263
""".strip().splitlines()
puzzle = open("puzzle_input").readlines()

print("ans1test", part1(p1_test))
print("ans1", part1(puzzle))


def part2(lines):
    seq = list(map(int, lines))
    threes = []
    window_size = 3
    for idx in range(len(seq) - window_size + 1):
        # print(seq[idx:idx + window_size])
        threes.append(sum(seq[idx:idx + window_size]))

    num_incr = sum(
        cur > prev for prev, cur in zip(threes[0:-1], threes[1:])
    )

    return num_incr


def part2_smartypants(lines):
    seq = list(map(int, lines))
    return sum(seq[idx+3] > seq[idx] for idx in range(len(seq)-3))


print("ans2test", part2(p1_test))
print("ans2", part2(puzzle))
print("ans2 smartypants", part2_smartypants(puzzle))
