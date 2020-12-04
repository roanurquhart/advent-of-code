import sys
from collections import Counter
from helpers import read_input

def password_philosophy_part1() :
    passwords = parse_input(read_input())
    count = 0
    for p in passwords:
        c = Counter(p.password)
        if c[p.letter] >= p.range[0] and c[p.letter] <= p.range[1]:
            count += 1
    print(count)

def password_philosophy_part2() :
    passwords = parse_input(read_input())
    count = 0
    for p in passwords:
        char_at_pos_1 = p.password[p.range[0]-1]
        char_at_pos_2 = p.password[p.range[1]-1]
        if (char_at_pos_1 != char_at_pos_2):
            if (p.letter == char_at_pos_1 or p.letter == char_at_pos_2):
                count += 1
    print(count)

## Classes
class Password:
    def __init__(self, range, letter, password):
        self.range = range
        self.letter = letter
        self.password = password

    def __repr__(self):
        return "<Password pass:%s range:%s letter:%s>" % (self.password, self.range, self.letter)

    def __str__(self):
        return "Password pass:%s range:%s letter:%s" % (self.password, self.range, self.letter)

## Parsers
def parse_input(data) :
    passwords = []
    for line in data:

        values = line.split()
        freq_range = values[0].split("-")
        letter = values[1][0]
        word = values[2]

        passwords.append(Password((int(freq_range[0]), int(freq_range[1])), letter, word));

    return passwords
