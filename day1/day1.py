f = open("alt-input.txt", "r", encoding="utf-8")
valid_digits_text = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
valid_digits_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

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
    def get_digits(s):
        i_digits = []
        i_digits.append(s.find(valid_digits_numbers))
        i_digits.append(s.rfind(valid_digits_numbers))
        print(i_digits)
        i_text = []
        i_text.append(s.find(valid_digits_text))
        i_text.append(s.rfind(valid_digits_text))
        print(i_text)
    for line in f:
        get_digits(line)

if __name__ == "__main__":
    #part_one()
    part_two()