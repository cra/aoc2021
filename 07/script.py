import functools
import numpy as np

test = "16,1,2,0,4,2,7,1,2,14"


def p1(initial):
    positions = list(map(int, initial.split(',')))
    m = np.median(positions)
    s = sum(abs(p-m) for p in positions)
    return m, s


print("P1 test", p1(test))
puzzle_input = open("./puzzle_input").readline().strip()
print("P1 real", p1(puzzle_input))


@functools.lru_cache
def calc_fuel_to_get_from_pos1_to_pos2(pos1, pos2):
    num_steps = abs(pos2 - pos1)
    total_fuel = num_steps / 2 * (num_steps + 1)
    return total_fuel


def p_monte(initial, n_iter=10_000):
    positions = list(map(int, initial.split(',')))
    low, high = min(positions), max(positions)
    min_pos = np.median(positions)
    min_cost = sum(calc_fuel_to_get_from_pos1_to_pos2(pos1, min_pos) for pos1 in positions)
    for i in range(n_iter):
        projected_min_pos = np.random.randint(low, high)
        new_cost = sum(calc_fuel_to_get_from_pos1_to_pos2(pos1, projected_min_pos) for pos1 in positions)
        if new_cost < min_cost:
            min_cost = new_cost
            print(f"on step {i} new min cost found: {min_cost}")
    return min_cost


print("P2 monte test", p_monte(test))
print("P2 monte puzzle", p_monte(puzzle_input))
