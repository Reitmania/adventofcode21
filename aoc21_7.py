import statistics

with open("aoc21_7_input.txt") as file:
    crabs = file.readline().split(",")
    crabs = list(map(int, crabs))

med = statistics.median(crabs)
fuel = 0
for crab in crabs:
    fuel += abs(crab - med)
print(fuel)
