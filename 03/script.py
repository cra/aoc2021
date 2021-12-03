import itertools

test = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""
test_lines = test.strip().splitlines()


def p1(lines, verbose=True):
    L = len(lines[0].strip())
    num0 = [0]*L
    num1 = [0]*L

    for line in lines:
        for i, ch in enumerate(line):
            if ch == "0":
                num0[i] += 1
            elif ch == "1":
                num1[i] += 1

    gamma = [0]*L
    eps = [0]*L
    for i in range(L):
        if num1[i] > num0[i]:
            gamma[i] = 1 
            eps[i] = 0
        else:
            gamma[i] = 0 
            eps[i] = 1

    gamma_s = ''.join(map(str, gamma))
    eps_s = ''.join(map(str, eps))
    if verbose:
        print(gamma_s)
        print(eps_s)

        print("p1:", int(gamma_s, 2) * int(eps_s, 2))
    return gamma_s, eps_s, num0, num1

def highlight_it(line, i):
    if i == 0:
        s = "".join(["_", line[0], "_", line[1:]])
        return s.strip()
    if i == len(line)-1:
        s = "".join([line[:-1], "_", line[-1], "_"])
        return s.strip()

    s = "".join([line[:i], "_", line[i], "_", line[i+1:]])
    return s.strip()


def find_most_common_in_pos_i(lines, i):
    bits = [line[i] for line in lines]
    num0 = bits.count("0")
    num1 = bits.count("1")
    return "1" if num1 >= num0 else "0"


def find_least_common_in_pos_i(lines, i):
    bits = [line[i] for line in lines]
    num0 = bits.count("0")
    num1 = bits.count("1")
    return "0" if num1 >= num0 else "1"


def p2(lines, verbose=True):
    L = len(lines[0].strip())
    orig_lines = lines[:]

    # search oxy
    print("Searching oxy")
    for i in range(L):
        most = find_most_common_in_pos_i(lines, i)
        tot = len(lines)
        idx_to_keep_oxy = {i: "whatever" for i in range(tot)}
        print(f"Pos: {i}. Most common value in this position for numbers that's left is {most}")
        print("Numbers:", ", ".join(map(highlight_it, lines, itertools.repeat(i))))
        for ii, line in enumerate(lines):
            bit = line[i]
            if ii in idx_to_keep_oxy:
                if bit != most:
                    print(f"    Bit not match most common -> removing {ii}:e line")
                    idx_to_keep_oxy.pop(ii)
                else:
                    print(f"    Bit matches, keeping {ii}:e line")
        print(f"Left with {len(idx_to_keep_oxy)} numbers for oxy")
        lines = [lines[i].strip() for i in idx_to_keep_oxy]
        print(", ".join(lines))

        if len(idx_to_keep_oxy) == 1:
            break

    oxy_rating_s = lines[0]
    oxy_rating = int(oxy_rating_s, 2)
    print(f"----> Oxy rating: {oxy_rating_s} (dec: {oxy_rating})")

    print("Searching co2")
    lines = orig_lines
    for i in range(L):
        least = find_least_common_in_pos_i(lines, i)
        tot = len(lines)
        idx_to_keep_co2 = {i: "whatever" for i in range(tot)}
        print(f"Pos: {i}. Least common value in this position for numbers that's left is {least}")
        print("Numbers:", ", ".join(map(highlight_it, lines, itertools.repeat(i))))
        for ii, line in enumerate(lines):
            bit = line[i]
            if ii in idx_to_keep_co2:
                if bit != least:
                    print(f"    Bit not match least common -> removing {ii}:e line")
                    idx_to_keep_co2.pop(ii)
                else:
                    print(f"    Bit matches, keeping {ii}:e line")
        print(f"Left with {len(idx_to_keep_co2)} numbers for co2")
        lines = [lines[i].strip() for i in idx_to_keep_co2]
        print(", ".join(lines))

        if len(idx_to_keep_co2) == 1:
            break

    co2_rating_s = lines[0]
    co2_rating = int(co2_rating_s, 2)
    print(f"----> co2 rating: {co2_rating_s} (dec: {co2_rating})")

    print("CO2 ind", idx_to_keep_co2)
    print("p2:", co2_rating * oxy_rating)


p1(test_lines)
puzzle_lines = open("./puzzle_input").readlines()
p1(puzzle_lines)

print("*"*30)
p2(test_lines)
p2(puzzle_lines)
