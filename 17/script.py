
import tqdm
import itertools
import re
from dataclasses import dataclass
test = "target area: x=20..30, y=-10..-5"


@dataclass
class Area:
    x0: int
    x1: int
    y0: int
    y1: int

    def is_point_inside(self, x, y):
        return (self.x0 <= x <= self.x1) and (self.y0 <= y <= self.y1)

    def am_i_above(self, x, y):
        return (self.x0 <= x <= self.x1) and y > max([self.y0, self.y1])

    def is_overshoot(self, x, y):
        return x > self.x1

    @classmethod
    def read_input(cls, inp_str):
        m = re.match("target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", inp_str)
        return cls(*list(map(int, m.groups())))


def p1(inp):
    target_area = Area.read_input(inp)
    highest = 0
    for vx, vy in itertools.product(range(1, target_area.x1+1), range(target_area.y0, 1000)):
        new_highest_candidate = 0
        we_waz_kingz = False
        x, y, v_x, v_y = 0, 0, vx, vy
        for i in range(1, 1000):  # 1000 steps should be enough
            y = y + v_y
            x = x + v_x
            if y > new_highest_candidate:
                new_highest_candidate = y
            if target_area.is_point_inside(x, y):
                we_waz_kingz = True
                break
            if v_x > 0:
                v_x -= 1
            if v_x == 0 and not target_area.am_i_above(x, y):
                # would never reach it
                break
            if target_area.is_overshoot(x, y):
                # too far
                break
            v_y -= 1
        if we_waz_kingz:
            if new_highest_candidate > highest:
                print(f"  New high at ({vx},{vy})={new_highest_candidate}")
                highest = new_highest_candidate
    return highest


def p2(inp):
    a = Area.read_input(inp)
    vv = set()
    steps_count = set()
    for tx, ty in tqdm.tqdm(
        itertools.product(
            range(a.x0, a.x1+1),
            range(a.y0, a.y1+1)
        ),
        total=((a.x1-a.x0)*abs(a.y0-a.y1))
    ):
        for vx, vy in itertools.product(range(1, tx+1), range(ty, 1000)):
            x, y, v_x, v_y = 0, 0, vx, vy
            for i in range(1, 1000):  # 1000 steps should be enough
                y = y + v_y
                x = x + v_x
                if x == tx and y == ty:
                    vv.add((vx, vy))
                    break
                if v_x > 0:
                    v_x -= 1
                if v_x == 0 and not x == tx:  # would never reach it
                    break
                if x > tx:  # too far
                    break
                v_y -= 1
            steps_count.add(i)
    print(steps_count)
    return len(vv)


if __name__ == '__main__':
    print("P1 test", p1(test))
    puz = open("./puzzle_input").readline().strip()
    print("P1 puz", p1(puz))

    print("P2 test", p2(test))
    print("P2 puz", p2(puz))
