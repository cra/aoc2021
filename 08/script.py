test = """
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


def p1(entries):
    number_easy_digits = 0
    for line in entries:
        _, rhs = line.split(" | ")
        l = list(map(len, rhs.split()))
        for num_segments in (2, 3, 4, 7):
            number_easy_digits += l.count(num_segments)
    return number_easy_digits


def solve_one_entry(entry):
    mappers = {ch: '' for ch in 'abcdefg'}
    lhs, rhs = entry.split(" | ")
    # find ones
    lhs_tokens = lhs.split()
    for token in lhs_tokens:
        if len(token) == 2:
            # this is the one
            for letter in token:
                mappers[letter] = ['c', 'f']
        if len(token) == 3:
            for letter in token:
                ...
                #if mappers[




def p2(entries):
    ...


if __name__ == '__main__':
    test = test.strip().splitlines()
    print("P1 test", p1(test))
    puzzle_input = [line.strip() for line in open("./puzzle_input").readlines()]
    print("P1 real", p1(puzzle_input))
