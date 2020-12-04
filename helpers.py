import sys

def read_input():
    with open(sys.argv[1], "r") as statefile:
        data = statefile.readlines()
    return data