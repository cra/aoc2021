
import time
import math
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
    (_, top), *_, (_, bot) = Counter(polymer).most_common()
    return top - bot


def polymer_to_paircount(polymer: List[str]):
    return Counter(''.join(pair) for pair in itertools.pairwise(polymer))


def evolve_paircounts_one_step(paircounts, singlecounts, rules):
    new_counts = Counter()
    for (a0, b0), pair_count in paircounts.items():
        new = rules[f'{a0}{b0}']
        new_counts.update({f'{a0}{new}': pair_count, f'{new}{b0}': pair_count})
        singlecounts.update({new:pair_count})
    return new_counts, singlecounts


def p2(inp, n_steps):
    """ p2 requires the pair mapper, it's lanterfish party all over again """
    polymer, rules = read_input(inp)
    singlecounts = Counter(polymer)
    paircounts = polymer_to_paircount(polymer)
    for i in range(1, n_steps+1):
        paircounts, singlecounts = evolve_paircounts_one_step(paircounts, singlecounts, rules)
    (_, top), *_, (_, bot) = singlecounts.most_common()
    return top - bot


if __name__ == '__main__':
    test = test.strip().splitlines()
    print("P1 test, 10 steps yields", p1(test, 10))
    puz = open("./puzzle_input").readlines()
    print("P1 puz, 10 steps yields", p1(puz, 10))

    print("---")
    print("P2 but test and 10 steps", p2(test, 10))
    print("P2 but test and 40 steps", p2(test, 40))
    print("P2 puz, 10 steps", p2(puz, 10))
    print("P2 puz, 40 steps", p2(puz, 40))