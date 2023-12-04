f = open("input.txt", "r", encoding="utf-8")
valid_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def part_one():
    n = 0
    for line in f:
        ns = []
        for c in line:
            if c.isdigit():
                ns.append(c)
        n += int(ns[0]+ns[-1])
    print(n)

def part_two():
    def check_if_valid(n):
        if n.isdigit():
            return True
        elseif 
