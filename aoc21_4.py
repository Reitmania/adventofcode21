import numpy as np

boards = list()

filename = "aoc21_4_input.txt"
with open(filename) as file:
    numbers = file.readline().split(",")
    count = 0
    boards.append(np.zeros(shape=(5,5)))
    for line in file:
        count += 1
        print(line.split(" "))

        if count == 5:
            count = 0
            boards.append(np.zeros(shape=(5,5)))
            

print(len(boards))