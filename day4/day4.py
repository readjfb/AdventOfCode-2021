class BingoBoard:
    def __init__(self, board_lines):
        self.board = [line.split() for line in board_lines]

        self.saved = [x.copy() for x in self.board]

        self.already_won = False

    def reset(self):
        self.board = [x.copy() for x in self.saved]
        self.already_won = False

    def place_token(self, token):
        for i in range(len(self.board)):
            self.board[i] = [" " if x == token else x for x in self.board[i]]

    def __str__(self):
        padded = [[x.ljust(4) for x in l] for l in self.board]
        return "\n".join([" ".join(x) for x in padded])

    def check_win(self):
        # Check rows
        for line in self.board:
            if not any(l != " " for l in line):
                return True
        # Check columns
        for i in range(len(self.board)):
            if not any(line[i] != " " for line in self.board):
                return True

        return False


sequence = ""

boards = []

with open("day4input.txt") as f:
    lines = f.readlines()

    sequence = lines[0].strip().split(",")

    rest = lines[2:]

i = 0
while i < len(rest):
    boards.append(BingoBoard(rest[i : i + 5]))

    i += 6

breakflag = False

S, N = 0, 0

for number in sequence:
    for board in boards:

        board.place_token(number)

        if board.check_win():
            s = 0
            for line in board.board:
                s += sum(int(x) for x in line if x != " ")

            S = s
            N = int(number)

            breakflag = True

            break
    if breakflag:
        break

print("Part 1:", S * N)

# Part 2
for board in boards:
    board.reset()

S, N = 0, 0

for number in sequence:
    for board in boards:

        board.place_token(number)

        if board.check_win() and not board.already_won:
            s = 0
            for line in board.board:
                s += sum(int(x) for x in line if x != " ")

            S = s
            N = int(number)

            board.already_won = True

print("Part 2:", S * N)
