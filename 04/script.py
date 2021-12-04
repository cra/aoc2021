import itertools
from io import StringIO

test = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


class Board:
    def __init__(self, board: dict):
        """ dict of form (i, j) -> (num, bool). Marked nums are (num, True) """
        self.board = board
        self.invert_board = {v:k for k,(v,_) in board.items()}

    def are_you_winning_son(self):
        for i in range(5):
            # check rows
            if all(self.board[i, j][1] for j in range(5)):
                return True
            # check cols
            if all(self.board[j, i][1] for j in range(5)):
                return True
        return False


    def mark(self, num):
        if num in self.invert_board:
            i, j = self.invert_board[num]
            v, _ = self.board[i, j]
            self.board[i, j] = v, True

    @property
    def sum_of_all_unmarked(self):
        s = 0
        for i, j in itertools.product(range(5), range(5)):
            v, t = self.board[i, j]
            s += v if not t else 0
        return s

    def score(self, winning_number):
        return self.sum_of_all_unmarked * winning_number


def build_numbers_seq_and_boards(lines):
    numbers = list(map(int, lines[0].split(',')))

    num_boards = sum(not line.strip() for line in lines[1:])
    boards = {i: {} for i in range(num_boards)}
    for i in range(num_boards):
        line_number = 1 + i*6
        assert not lines[line_number].strip()
        for ii, j in enumerate(range((line_number+1), (line_number+1)+5)):
            for kk, num in enumerate(map(int, lines[j].strip().split())):
                boards[i][(ii, kk)] = (num, False)

    return numbers, boards


def p1(lines):
    numbers, boards = build_numbers_seq_and_boards(lines)
    boards = list(map(Board, boards.values()))
    for i, num in enumerate(numbers):
        #print("nnnnnnumber", num)
        for b in boards:
            b.mark(num)
        if i < 5:
            continue
        #print("checking winning boards")
        for ii, b in enumerate(boards, start=1):
            if b.are_you_winning_son():
                print(f"Board #{ii} is winning!!!")
                print("  Board score:", b.score(num))
                return
            #print(f"Board #{ii} is not winning yet")

print("Test run")
p1(test.strip().splitlines())
print("P1 run")
p1(open("./puzzle_input").readlines())

# find the one that wins last
def p2(lines):
    numbers, boards = build_numbers_seq_and_boards(lines)
    boards = {i: Board(v) for i, v in boards.items()}
    for i, num in enumerate(numbers):
        for b in boards.values():
            b.mark(num)
        if i < 5:
            continue
        boards_to_kick = []
        for ii, b in boards.items():
            if b.are_you_winning_son():
                print(f"Board #{ii} is winning!!!")
                boards_to_kick.append(ii)
                if len(boards) == 1:
                    print("  Board score:", b.score(num))
                    print("This is the last one btw^^^")
                    return

        for b_num in boards_to_kick:
            boards.pop(b_num)

print("P2 run")
p2(open("./puzzle_input").readlines())
