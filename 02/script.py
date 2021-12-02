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

my_start = [0, 0]
for d, v in dirs:
    if d == "forward":
        my_start[0] += v
    if d == "down":
        my_start[1] += v
    if d == "up":
        my_start[1] -= v

print(my_start, my_start[0] * my_start[1])


# -- part 2

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

print(pos, pos[0] * pos[1])
