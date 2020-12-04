from helpers import read_input

def toboggan_trajectory_part1(slope) :
    geography = parse_input(read_input())
    count = count_trees_collisions(geography, slope[0], slope[1])
    print(count)

def toboggan_trajectory_part2(slopes) :
    geography = parse_input(read_input())
    product = 1
    for slope in slopes:
        product *= count_trees_collisions(geography, slope[0], slope[1])
    print(product)

def count_trees_collisions(geography, run, drop) :
    count = 0
    row = 1
    column = LimitedInt(len(geography[0])-1, run)
    column.increment_value()
    while (row < len(geography)) :
        if (geography[row][column.value] == "#") :
            count += 1
            print(str(row) + ":" + str(column.value) + ":X")
        else :
            print(str(row) + ":" + str(column.value) + ":0")
        column.increment_value()
        row += drop
    print(count)
    return count

def parse_input(data):
    geography = []
    for line in data :
        geography.append(line.rstrip())
    return geography

class LimitedInt :
    def __init__(self, limit, slope):
        self.value = 0
        self.slope = slope
        self.limit = limit
    
    def increment_value(self):
        if (self.value + self.slope > self.limit):
            self.value = self.value + self.slope - self.limit-1
        else :
            self.value  += self.slope