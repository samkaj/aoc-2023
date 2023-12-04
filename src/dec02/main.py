#!/usr/bin/env python3

bag = {"red": 12, "green": 13, "blue": 14}


def get_lines(path):
    lines = []
    with open(path, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def rgb(line: str):
    pairs = line.split(", ")
    r, g, b = 0, 0, 0
    for pair in pairs:
        pair = pair.strip()
        splits = pair.split(" ")
        amount = splits[0]
        color = splits[1]
        if color == "red":
            r = int(amount)
        if color == "green":
            g = int(amount)
        if color == "blue":
            b = int(amount)
    return (r, g, b)


def part_one(line: str):
    parts = line.split(":")
    round_id = parts[0][5:]
    rounds = parts[1].split(";")
    for round in rounds:
        colors = rgb(round)
        if bag["red"] < colors[0] or bag["green"] < colors[1] or bag["blue"] < colors[2]:
            return 0
    return int(round_id)


def part_two(line: str):
    parts = line.split(":")
    rounds = parts[1].split(";")
    max_r, max_g, max_b = 0, 0, 0
    for round in rounds:
        colors = rgb(round)
        if colors[0] > max_r:
            max_r = colors[0]
        if colors[1] > max_g:
            max_g = colors[1]
        if colors[2] > max_b:
            max_b = colors[2]
    return max_r * max_g * max_b


def main():
    tot = 0
    for line in get_lines("in.txt"):
        tot += part_one(line)
    print(f"Part one: {tot}")
    tot = 0
    for line in get_lines("in.txt"):
        tot += part_two(line)
    print(f"Part two: {tot}")


if __name__ == "__main__":
    main()
