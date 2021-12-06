'''
--- Day 5: Hydrothermal Venture ---

You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2

Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

    An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
    An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.

For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....

In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

'''
import numpy as np

def parseInput():
    # Using readlines()
    filename = "aoc21_5_input.txt"
    with open(filename) as file:
        lines = file.readlines()

    x = list()   
    y = list() 
    for line in lines:    
        line = str.split(line)
        line.pop(1)
        x1,y1 = line[0].split(",") 
        x2,y2 = line[1].split(",")
        x.append([int(x1),int(x2)])    
        y.append([int(y1),int(y2)])  
    return x,y

def main():
    x,y = parseInput()
    #print(x[0])
    xmax = int(max(max(x))) 
    ymax = int(max(max(y)))   
    array = np.zeros((xmax, ymax))
    for i in range(len(x)):
        x1 = x[i][0]
        x2 = x[i][1]
        y1 = y[i][0]
        y2 = y[i][1]
        #only vertical and horizontal
        if x1 == x2:
            ycoord = np.sort(y[i])
            for k in range(ycoord[0],ycoord[1]+1):
                array[x1][k] += 1
        elif y1 == y2:
            xcoord = np.sort(x[i])
            for k in range(xcoord[0],xcoord[1]+1):
                array[k][y1] += 1
        else:
            #diagonal
            ycoord = np.sort(y[i])
            xcoord = np.sort(x[i])
            for k in range(ycoord[1]-ycoord[0]+1):
                array[xcoord[0]+k][ycoord[0]+k] += 1

    count = 0
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] > 1:
                count += 1
    print(count)


main()