#!/usr/bin/env python3

nums = '1234567890'
specials = '/=*@+#%$&'


class Num:
    def __init__(self, row, col, val) -> None:
        self.row = row
        self.col = col
        self.val = val
        self.matched = False

    def __str__(self) -> str:
        if self.val not in specials:
            return f"({self.row}, {self.col}:{self.col+len(self.val)}) -> {self.val}"
        return f"({self.row}, {self.col}) -> {self.val}"


def get_lines(path) -> list[str]:
    lines = []
    with open(path, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def get_nums(lines: list[str]):
    values = []
    is_num = False
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char in nums:
                if not is_num:
                    values.append(Num(row, col, char))
                    is_num = True
                else:
                    values[-1].val += char
            else:
                is_num = False
    return values


def get_parts(lines: list[str]):
    parts = []
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char in specials:
                parts.append(Num(row, col, char))
    return parts


def part1(nums, parts) -> int:
    tot = 0
    for num in nums:
        for part in parts:
            found = False
            same_row = part.row == num.row
            above_row = num.row == part.row - 1
            below_row = num.row == part.row + 1
            if not (same_row or above_row or below_row):
                continue
            left = part.col == num.col - 1
            right = part.col == num.col + len(num.val)
            if same_row and (left or right):
                found = True
            for i in range(num.col - 1, num.col + len(num.val)+1):
                if part.col == i:
                    found = True
                    break
            if found and not num.matched:
                tot += int(num.val)
                num.matched = True
                print(part, " - ", num)
    return tot


def main():
    lines = get_lines("input.txt")
    vals = get_nums(lines)
    parts = get_parts(lines)
    print(part1(vals, parts))


if __name__ == "__main__":
    main()
