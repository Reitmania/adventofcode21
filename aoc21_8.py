'''
0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

'''

inputs = list()
outputs = list()

with open("aoc21_8_input.txt") as file:
    for line in file:
        patterns = line.split("|")
        inputs.append(patterns[0].split(" ")[0:10])
        output = patterns[1].split(" ")[1:5]
        output[3] = output[3].rstrip()
        print(output)
        outputs.append(output)

# 1: 2
# 4: 4
# 7: 3
# 8: 7
count = 0
for output in outputs:
    for digit in output:
        if (len(digit) == 2) or (len(digit) == 3) or (len(digit) == 4) or (len(digit) == 7):
            #print(digit)
            count += 1
print(count)