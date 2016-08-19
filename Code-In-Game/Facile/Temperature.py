import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526

templist = temps.split(" ")
print("Value templist :", file=sys.stderr)
print(templist, file=sys.stderr)

if n == 0:
    print("0")
elif n == 1:
    mini = temps
else:
    mini = 9999
    diff_mini = abs(mini)
    
    for t in templist:
        t = int(t)
        diff = abs(t)

        if diff < diff_mini:
            mini = t
            diff_mini = abs(diff)
        elif diff == diff_mini and t > mini:
            mini = t
            diff_mini = abs(diff)
        elif diff == diff_mini and t == mini:
            mini = t
            diff_mini = abs(diff)
            
    print(mini)
