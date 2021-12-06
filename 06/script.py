import collections
import copy
test = "3,4,3,1,2"


def evolve(fishes: list[int]):
    new_fishes = []
    newborns = []
    for fish in fishes:
        if fish == 0:
            new_fishes.append(6)
            newborns.append(8)
        else:
            new_fishes.append(fish - 1)
    new_fishes.extend(newborns)
    return new_fishes


def p1(initial: str, verbose18=False, ndays=80):
    fishes = list(map(int,initial.split(',')))
    if verbose18:
        print("Initial fishes:", ','.join(map(str,fishes)))
        for i in range(1, 19):
            fishes = evolve(fishes)
            print(f"After {i} days (tot={len(fishes)})", ','.join(map(str,fishes)))
            print("freq", {i: fishes.count(i) for i in set(fishes)})
        return
    for _ in range(ndays):
        fishes = evolve(fishes)
    print(f"after {ndays} days:", len(fishes))


def p1_1(initial: str, ndays=80):
    fishes = list(map(int,initial.split(',')))
    fish_freq = {i: fishes.count(i) for i in set(fishes)}
    for _ in range(ndays):
        new_fish_freq = {}
        for num in fish_freq:
            if num == 0:
                continue
            new_fish_freq[num-1] = fish_freq[num]
        if 0 in fish_freq:
            new_fish_freq[6] = new_fish_freq.get(6, 0) + fish_freq[0]
            new_fish_freq[8] = fish_freq[0]
        # print(new_fish_freq)
        fish_freq = copy.deepcopy(new_fish_freq)
    print(f'blurp after {ndays}', sum(fish_freq.values()))


if __name__ == '__main__':
    p1(test, verbose18=True)
    p1(test)
    p1_1(test)

    print("Single '1'")
    p1('1', verbose18=False, ndays=40)
    p1('1', verbose18=False, ndays=60)
    p1('1', verbose18=False, ndays=80)
 
    print("Single '1' using 1_1")
    p1_1('1', ndays=40)
    p1_1('1', ndays=60)
    p1_1('1', ndays=80)

    print("Bamboozle!!!")
    puzzle=open("./puzzle_input").readline().strip()
    print("real data, p1_1")
    p1_1(puzzle)
    p1_1(puzzle, ndays=256)
 
