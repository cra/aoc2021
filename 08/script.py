import itertools
import collections
import operator

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

TOP, TL, TR, MID, BL, BR, BOT = 'TOP', 'TL', 'TR', 'MID', 'BL', 'BR', 'BOT'

NUMS_TO_SEGMS = {
    0: (TOP, TL, TR, BL, BR, BOT),
    1: (TR, BR),
    2: (TOP, TR, MID, BL, BOT),
    3: (TOP, TR, MID, BR, BOT),
    4: (TL, TR, MID, BR),
    5: (TOP, TL, MID, BR, BOT),
    6: (TOP, TL, MID, BL, BR, BOT),
    7: (TOP, TR, BR),
    8: (TOP, TL, TR, MID, BL, BR, BOT),
    9: (TOP, TL, TR, MID, BR, BOT),
}


def p1(entries):
    number_easy_digits = 0
    for line in entries:
        _, rhs = line.split(" | ")
        l = list(map(len, rhs.split()))
        for num_segments in (2, 3, 4, 7):
            number_easy_digits += l.count(num_segments)
    return number_easy_digits


def find_mapping_for_one_entry(entry, verbose=False):
    mappers = {ch: None for ch in 'abcdefg'}
    lhs, _ = entry.split(" | ")
    lhs_tokens = lhs.split()

    # find BL, the only that has 4 occurencies
    # fintd BR, the only that has 9 occurencies
    cnt = collections.Counter(''.join(lhs_tokens))
    if verbose: print(cnt.most_common())
    for k, v in cnt.most_common():
        if v == 4:
            mappers[k] = BL
        if v == 6:  # FUUUUUCK this makes everything MUCH simplier
            mappers[k] = TL
        if v == 9:
            mappers[k] = BR

    # find number 1
    token = next(token for token in lhs_tokens if len(token) == 2)
    if verbose: print('found 2-symbols token', token)
    for letter in (letter for letter in token if mappers[letter] != BR):
        mappers[letter] = TR
    lhs_tokens.remove(token)

    # find number 7: the only letter with three segments
    token = next(token for token in lhs_tokens if len(token) == 3)
    if verbose: print('found 3-symbols token', token)
    for letter in token:
        if any(mappers[letter] == seg for seg in (TR, BR)):  # that's a side one
            continue
        mappers[letter] = TOP
    lhs_tokens.remove(token)

    # find number 4: the only letter with four segments
    token = next(token for token in lhs_tokens if len(token) == 4)
    if verbose: print('found 4-symbols token', token)
    for letter in token:
        if any(mappers[letter] == seg for seg in [TL, TR, BR]):  # known so far
            continue
        mappers[letter] = MID
    lhs_tokens.remove(token)

    # find number 8: the only letter with eight segments
    token = next(token for token in lhs_tokens if len(token) == 7)
    if verbose: print('found 7-symbols token', token)
    mappers[next(seg for seg in token if mappers[seg] == None)] = BOT
    lhs_tokens.remove(token)

    return mappers


def solve_one_entry(entry, verbose=False):
    if verbose: print(entry)
    mappers = find_mapping_for_one_entry(entry, verbose=verbose)
    inverse_mappers = {v:k for k,v in mappers.items()}
    if verbose: print("inverse mappers",inverse_mappers)

    TRANSLATION = {}
    for num, segments in NUMS_TO_SEGMS.items():
        scrambled_letters = (inverse_mappers[segment] for segment in segments)
        sorted_letters = ''.join(sorted(scrambled_letters))
        TRANSLATION[sorted_letters] = num

    if verbose: print("Found translation", TRANSLATION)

    rhs_tokens = entry.split(" | ")[1].split()
    if verbose: print("Here are rhs:", rhs_tokens)
    reading = ''
    for token in rhs_tokens:
        ordered_token  = ''.join(sorted(token))
        num = str(TRANSLATION[ordered_token])
        if verbose: print(f'{token} -> {num}')
        reading += num

    return int(reading)


def p2(entries, verbose=False):
    return sum(map(solve_one_entry, entries, itertools.repeat(verbose)))


if __name__ == '__main__':
    test = test.strip().splitlines()
    print("P1 test", p1(test))
    puzzle_input = [line.strip() for line in open("./puzzle_input").readlines()]
    print("P1 real", p1(puzzle_input))
    print("P2 test", p2(test))
    print("P2 real", p2(puzzle_input))
