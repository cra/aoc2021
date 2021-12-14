import itertools
from collections import Counter
from typing import List

test = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

def read_input(inp: List[str]):
    template = inp[0].strip()
    rules = {}
    for line in inp[2:]:
        lhs, rhs = line.strip().split(" -> ")
        rules[lhs] = rhs

    return template, rules


def evolve_one_step(polymer, rules):
    polymer = list(polymer)
    new_insertions = {}
    for pos, pair in enumerate(itertools.pairwise(polymer), start=1):
        if (lhs := ''.join(pair)) in rules:
            new_insertions[pos] = rules[lhs]
    for shift, (pos, element) in enumerate(new_insertions.items()):
        polymer.insert(pos+shift, element)
    return ''.join(polymer)


def p1(inp, n_steps):
    polymer, rules = read_input(inp)
    for _ in range(n_steps):
        polymer = evolve_one_step(polymer, rules)
    cnt = Counter(polymer).most_common()
    # print(cnt[0], cnt[-1])
    return cnt[0][1] - cnt[-1][1]


if __name__ == '__main__':
    test = test.strip().splitlines()
    print("P1 test, 10 steps yields", p1(test, 10))
    puz = open("./puzzle_input").readlines()
    print("P1 puz, 10 steps yields", p1(puz, 10))
    # --
    print("P2 test: same rules, 40 steps. It yields", p1(test, 40))