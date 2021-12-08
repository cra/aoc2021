import collections

test: str = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""


TOP = 'a'
TL = 'b'
TR = 'c'
MID = 'd'
BL = 'e'
BR = 'f'
BOT = 'g'

STAT10 = {
    TOP: 8,
    TL: 6,
    TR: 8,
    MID: 7,
    BL: 4,
    BR: 9,
    BOT: 7,
}


def p1(entries):
    number_easy_digits = 0
    for line in entries:
        _, rhs = line.split(" | ")
        l = list(map(len, rhs.split()))
        for num_segments in (2, 3, 4, 7):
            number_easy_digits += l.count(num_segments)
    return number_easy_digits


def solve_one_entry(entry):
    mappers = {ch: [] for ch in 'abcdefg'}
    lhs, rhs = entry.split(" | ")
    lhs_tokens = lhs.split()

    # find BL, the only that has 4 occurencies
    cnt = collections.Counter(''.join(lhs_tokens))
    for k, v in cnt.most_common():
        if v == 4:
            for kk in mappers:
                if BL in mappers[kk]:
                    mappers[kk].remove(BL)
            mappers[k] = [BL]

    # find number one
    for token in lhs_tokens:
        if len(token) == 2:
            print('found 2-symbols token', token)
            for letter in token:
                mappers[letter] = [TR, BR]
            lhs_tokens.remove(token)
            break
    # find number 7: the only letter with three segments
    for token in lhs_tokens:
        if len(token) == 3:
            print('found 3-symbols token', token)
            for letter in token:
                if (TR in mappers[letter]) or (BR in mappers[letter]):  # that's a side one
                    continue
                mappers[letter] = [TOP]
            lhs_tokens.remove(token)
            break
    # find number 4: the only letter with four segments
    for token in lhs_tokens:
        if len(token) == 4:
            print('found 4-symbols token', token)
            for letter in token:
                if (TR in mappers[letter]) or (BR in mappers[letter]):  # that's a side one
                    mappers[letter] = [TL, MID]
            lhs_tokens.remove(token)
            break
    # find number 8: the only letter with eight segments
    for token in lhs_tokens:
        if len(token) == 8:
            print('found 8-symbols token', token)
            for letter in token:
                if any(
                    TOP in mappers[letter],
                    TL in mappers[letter],
                    TR in mappers[letter],
                    MID in mappers[letter],
                    BR in mappers[letter],
                    BL in mappers[letter],
                ):
                    continue
                mappers[letter] = [BOT]
            lhs_tokens.remove(token)
            break
    # since lhs_tokens was modified we can't recalc now, or can we?
    # bottom left is the only one that is present in 7 positions

    print("Known mappers", mappers)
    print("Left with tokens", lhs_tokens)


def p2(entries):
    solve_one_entry(entries[0])


if __name__ == '__main__':
    test = test.strip().splitlines()
    print("P1 test", p1(test))
    #puzzle_input = [line.strip() for line in open("./puzzle_input").readlines()]
    #print("P1 real", p1(puzzle_input))
    print("P2 test", p2(test))
